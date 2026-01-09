"""Image copying operations."""

import shutil
from pathlib import Path

from models import ImageMetadata
from indexer import ImageIndexer


class ImageCopier:
    """Handles copying images to destination."""
    
    def __init__(self, indexer: ImageIndexer):
        self.indexer = indexer
        self.copied = 0
        self.not_found = 0
    
    def copy(self, metadata: ImageMetadata, dest_dir: Path) -> bool:
        """Copy image to destination directory."""
        source = self.indexer.find(metadata.filename)
        
        if not source:
            self.not_found += 1
            return False
        
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / metadata.filename
        
        shutil.copy2(source, dest)
        self.copied += 1
        return True
    
    def reset_stats(self) -> None:
        """Reset statistics."""
        self.copied = 0
        self.not_found = 0
    
    def print_stats(self, label: str) -> None:
        """Print copy statistics."""
        print(f"  {label}: copied={self.copied}, not_found={self.not_found}")

