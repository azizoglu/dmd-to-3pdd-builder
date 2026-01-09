"""Dataset structure builders."""

from pathlib import Path
from typing import List
from abc import ABC, abstractmethod

from file_utils import ClassMapper
from indexer import ImageIndexer
from parser import TextFileParser
from copier import ImageCopier


class DatasetBuilder(ABC):
    """Base class for dataset builders."""
    
    SPLITS = ['train', 'val', 'test']
    
    def __init__(
        self,
        output_dir: Path,
        class_mapper: ClassMapper,
        indexer: ImageIndexer,
        txt_dir: Path
    ):
        self.output_dir = output_dir
        self.parser = TextFileParser(class_mapper)
        self.copier = ImageCopier(indexer)
        self.txt_dir = txt_dir
    
    @abstractmethod
    def build(self, perspectives: List[str]) -> None:
        """Build dataset structure."""
        pass


class SplitBuilder(DatasetBuilder):
    """Builds dataset with train/val/test splits."""
    
    def build(self, perspectives: List[str]) -> None:
        """Build split structure: perspective/split/class/images"""
        print("\nBuilding split structure...")
        
        for perspective in perspectives:
            print(f"\n{perspective.upper()}:")
            
            for split in self.SPLITS:
                self.copier.reset_stats()
                self._process(perspective, split)
                self.copier.print_stats(split)
    
    def _process(self, perspective: str, split: str) -> None:
        """Process one perspective-split combination."""
        txt_file = self.txt_dir / f"{perspective}_{split}_images.txt"
        metadata_list = self.parser.parse(txt_file)
        
        for metadata in metadata_list:
            dest_dir = self.output_dir / perspective / split / metadata.class_name
            self.copier.copy(metadata, dest_dir)


class FlatBuilder(DatasetBuilder):
    """Builds flat dataset without splits."""
    
    def build(self, perspectives: List[str]) -> None:
        """Build flat structure: perspective/class/images"""
        print("\nBuilding flat structure...")
        
        for perspective in perspectives:
            print(f"\n{perspective.upper()}:")
            self.copier.reset_stats()
            
            for split in self.SPLITS:
                self._process(perspective, split)
            
            self.copier.print_stats("total")
    
    def _process(self, perspective: str, split: str) -> None:
        """Process one perspective-split, merge into flat structure."""
        txt_file = self.txt_dir / f"{perspective}_{split}_images.txt"
        metadata_list = self.parser.parse(txt_file)
        
        for metadata in metadata_list:
            dest_dir = self.output_dir / perspective / metadata.class_name
            self.copier.copy(metadata, dest_dir)

