"""Text file parser for image lists."""

from pathlib import Path
from typing import List, Optional

from models import ImageMetadata
from file_utils import ClassMapper


class TextFileParser:
    """Parses image list text files."""
    
    def __init__(self, class_mapper: ClassMapper):
        self.class_mapper = class_mapper
    
    def parse(self, txt_file: Path) -> List[ImageMetadata]:
        """Parse text file and return image metadata list."""
        if not txt_file.exists():
            return []
        
        metadata_list = []
        
        with open(txt_file, 'r', encoding='utf-8') as f:
            for line in f:
                metadata = self._parse_line(line.strip())
                if metadata:
                    metadata_list.append(metadata)
        
        return metadata_list
    
    def _parse_line(self, line: str) -> Optional[ImageMetadata]:
        """Parse single line: 'filename.jpg 0'"""
        if not line:
            return None
        
        parts = line.split()
        if len(parts) != 2:
            return None
        
        filename = parts[0]
        
        try:
            class_idx = int(parts[1])
        except ValueError:
            return None
        
        class_name = self.class_mapper.get_class_name(class_idx)
        if not class_name:
            return None
        
        return ImageMetadata(
            filename=filename,
            class_idx=class_idx,
            class_name=class_name
        )

