"""User interface for dataset builder."""

from pathlib import Path
from typing import List


class UI:
    """Handles user interaction."""
    
    @staticmethod
    def get_directory() -> Path:
        """Get source directory from user."""
        while True:
            path_str = input("\nSource directory path: ").strip()
            path = Path(path_str)
            
            if path.exists() and path.is_dir():
                return path
            
            print(f"Error: Directory not found: {path_str}")
    
    @staticmethod
    def get_perspectives() -> List[str]:
        """Get perspective selection from user."""
        options = ['body', 'face', 'hands']
        return UI._multi_choice("Select perspectives:", options)
    
    @staticmethod
    def get_structure() -> str:
        """Get structure type from user."""
        options = ['split', 'flat']
        return UI._single_choice("Structure type:", options)
    
    @staticmethod
    def confirm_overwrite(path: Path) -> bool:
        """Confirm overwriting existing directory."""
        response = input(f"\nWarning: '{path}' exists. Overwrite? (y/n): ").lower()
        return response in ['y', 'yes']
    
    @staticmethod
    def _single_choice(prompt: str, options: List[str]) -> str:
        """Get single choice from user."""
        print(f"\n{prompt}")
        for i, opt in enumerate(options, 1):
            print(f"  {i}. {opt}")
        
        while True:
            try:
                idx = int(input("Choice: ")) - 1
                if 0 <= idx < len(options):
                    return options[idx]
            except (ValueError, KeyboardInterrupt):
                raise KeyboardInterrupt
            print("Invalid choice")
    
    @staticmethod
    def _multi_choice(prompt: str, options: List[str]) -> List[str]:
        """Get multiple choices from user."""
        print(f"\n{prompt}")
        for i, opt in enumerate(options, 1):
            print(f"  {i}. {opt}")
        print("  0. All")
        
        while True:
            try:
                choice = input("Choices (comma-separated): ").strip()
                
                if choice == "0":
                    return options
                
                indices = [int(c.strip()) - 1 for c in choice.split(',')]
                selected = [options[i] for i in indices if 0 <= i < len(options)]
                
                if selected:
                    return selected
            except (ValueError, KeyboardInterrupt):
                raise KeyboardInterrupt
            print("Invalid choice")

