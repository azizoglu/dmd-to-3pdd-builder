"""Image indexing for fast lookups."""

import os
import time
from pathlib import Path
from typing import Dict, Optional, List, Tuple
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import cpu_count

from file_utils import FileNormalizer


def _is_image_file(filename: str, extensions: set) -> bool:
    """Check if file is supported image format."""
    return Path(filename).suffix.lower() in extensions


def _scan_directory_worker(args: Tuple[str, set]) -> List[Tuple[str, str]]:
    """
    Worker function to scan a single directory (non-recursive).
    Returns list of (filename, full_path) tuples.
    """
    dirpath, extensions = args
    results = []
    
    try:
        with os.scandir(dirpath) as entries:
            for entry in entries:
                if entry.is_file(follow_symlinks=False):
                    if _is_image_file(entry.name, extensions):
                        results.append((entry.name, entry.path))
    except (PermissionError, OSError):
        pass
    
    return results


class ImageIndexer:
    """Indexes images from source directory with parallel processing."""
    
    EXTENSIONS = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.gif', '.webp'}
    
    def __init__(self):
        self._exact_index: Dict[str, str] = {}
        self._normalized_index: Dict[str, str] = {}
    
    def index_directory(self, source_dir: Path, max_workers: Optional[int] = None) -> int:
        """
        Recursively index all images in directory using parallel processing.
        Returns number of images indexed.
        
        Args:
            source_dir: Root directory to scan
            max_workers: Number of worker processes (default: CPU count)
        """
        print(f"Indexing: {source_dir}")
        print(f"Scanning directories for images...")
        
        if max_workers is None:
            max_workers = max(1, cpu_count() - 1)  # Leave one CPU free
        
        print(f"Using {max_workers} parallel workers\n")
        
        # Stream-based approach: discover and process simultaneously
        start_time = time.time()
        last_update_time = start_time
        dir_count = 0
        processed_count = 0
        
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            futures = {}
            
            try:
                # Walk through directories
                for root, dirs, _ in os.walk(source_dir):
                    # Submit this directory for processing
                    future = executor.submit(_scan_directory_worker, (root, self.EXTENSIONS))
                    futures[future] = root
                    dir_count += 1
                    
                    # Show discovery progress every 100 directories or every 1 second
                    current_time = time.time()
                    if (dir_count % 100 == 0) or (current_time - last_update_time >= 1.0):
                        elapsed = current_time - start_time
                        rate = dir_count / elapsed if elapsed > 0 else 0
                        print(f"  Discovering: {dir_count:,} dirs found "
                              f"({rate:.0f} dirs/s) - {len(self._exact_index):,} images indexed", 
                              end='\r', flush=True)
                        last_update_time = current_time
                    
                    # Process completed results to avoid queue buildup
                    done_futures = [f for f in futures if f.done()]
                    for future in done_futures:
                        try:
                            results = future.result()
                            for filename, full_path in results:
                                self._add(filename, full_path)
                            processed_count += 1
                        except Exception as e:
                            print(f"\n  Warning: Error processing directory: {e}")
                        del futures[future]
                
            except (PermissionError, OSError) as e:
                print(f"\n  Warning during directory walk: {e}")
            
            # Final pass: process remaining futures
            print(f"\n  Finalizing: {dir_count:,} directories discovered, "
                  f"waiting for {len(futures):,} to complete...", flush=True)
            
            for future in as_completed(futures):
                try:
                    results = future.result()
                    for filename, full_path in results:
                        self._add(filename, full_path)
                    processed_count += 1
                    
                    # Show final processing progress
                    current_time = time.time()
                    if (processed_count % 100 == 0) or (current_time - last_update_time >= 1.0):
                        remaining = len(futures) - (processed_count - (dir_count - len(futures)))
                        print(f"  Processing: {processed_count:,}/{dir_count:,} "
                              f"({remaining:,} remaining) - {len(self._exact_index):,} images", 
                              end='\r', flush=True)
                        last_update_time = current_time
                        
                except Exception as e:
                    print(f"\n  Warning: Error processing directory: {e}")
        
        elapsed = time.time() - start_time
        count = len(self._exact_index)
        print(f"\n\n✓ Indexed: {count:,} images from {dir_count:,} directories in {elapsed:.1f}s")
        return count
    
    def find(self, filename: str) -> Optional[str]:
        """Find image using exact or normalized matching."""
        if filename in self._exact_index:
            return self._exact_index[filename]
        
        normalized = FileNormalizer.normalize(filename)
        return self._normalized_index.get(normalized)
    
    def _add(self, filename: str, full_path: str) -> None:
        """Add to both indices."""
        self._exact_index[filename] = full_path
        
        normalized = FileNormalizer.normalize(filename)
        if normalized not in self._normalized_index:
            self._normalized_index[normalized] = full_path

