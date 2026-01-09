#!/usr/bin/env python3
"""
3PDD Dataset Builder

Organizes images from source directory into structured 3PDD dataset
based on text file listings and class indices.
"""

import shutil
from pathlib import Path

from file_utils import ClassMapper
from indexer import ImageIndexer
from builders import SplitBuilder, FlatBuilder
from ui import UI


class DatasetBuilderApp:
    """Main application orchestrator."""
    
    def __init__(self):
        self.ui = UI()
        self.class_mapper = ClassMapper(Path("class_to_idx.json"))
    
    def run(self) -> None:
        """Execute workflow."""
        self._print_header()
        
        source_dir = self.ui.get_directory()
        
        indexer = ImageIndexer()
        indexer.index_directory(source_dir)
        
        perspectives = self.ui.get_perspectives()
        structure = self.ui.get_structure()
        
        output_dir = Path("3pdd")
        self._prepare_output(output_dir)
        
        builder = self._create_builder(structure, output_dir, indexer)
        
        print("\n" + "=" * 50)
        builder.build(perspectives)
        print("\n" + "=" * 50)
        print(f"Complete! Output: {output_dir.absolute()}")
        print("=" * 50)
    
    def _print_header(self) -> None:
        """Print header."""
        print("=" * 50)
        print("3PDD Dataset Builder")
        print("=" * 50)
    
    def _prepare_output(self, output_dir: Path) -> None:
        """Prepare output directory."""
        if output_dir.exists():
            if self.ui.confirm_overwrite(output_dir):
                shutil.rmtree(output_dir)
            else:
                raise SystemExit("Cancelled")
    
    def _create_builder(self, structure: str, output_dir: Path, indexer: ImageIndexer):
        """Create appropriate builder."""
        txt_dir = Path("image_lists")
        
        if structure == 'split':
            return SplitBuilder(output_dir, self.class_mapper, indexer, txt_dir)
        else:
            return FlatBuilder(output_dir, self.class_mapper, indexer, txt_dir)


def main():
    """Entry point."""
    try:
        app = DatasetBuilderApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nCancelled")
    except Exception as e:
        print(f"\nError: {e}")
        raise


if __name__ == "__main__":
    main()
