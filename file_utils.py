"""File handling utilities."""

import re
import json
from pathlib import Path
from typing import Dict, Optional


class FileNormalizer:
    """Normalizes filenames for flexible matching."""
    
    SPECIAL_CHARS = r'[_\-;:,\.\s]+'
    
    @classmethod
    def normalize(cls, filename: str) -> str:
        """
        Remove special characters from filename for matching.
        
        Example: "image_2019-03-15;13.jpg" -> "image20190315"
        """
        stem = Path(filename).stem
        normalized = re.sub(cls.SPECIAL_CHARS, '', stem)
        return normalized.lower()


class ClassMapper:
    """Manages class name to index mappings."""
    
    def __init__(self, mapping_file: Path):
        self.class_to_idx = self._load(mapping_file)
        self.idx_to_class = {v: k for k, v in self.class_to_idx.items()}
    
    def _load(self, file_path: Path) -> Dict[str, int]:
        """Load mapping from JSON file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def get_class_name(self, idx: int) -> Optional[str]:
        """Get class name by index."""
        return self.idx_to_class.get(idx)

