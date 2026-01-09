"""Data models for dataset builder."""

from dataclasses import dataclass


@dataclass
class ImageMetadata:
    """Represents metadata for a single image."""
    filename: str
    class_idx: int
    class_name: str

