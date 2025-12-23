#!/usr/bin/env python3
"""
Chapter 10: Python Projects for Beginners
Project 4: File Organizer

Organize files in a directory by extension.
"""

import os
import shutil
from pathlib import Path
from collections import defaultdict

class FileOrganizer:
    def __init__(self, source_dir="."):
        self.source_dir = Path(source_dir)

        # Define file categories
        self.categories = {
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
            "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
            "Spreadsheets": [".xls", ".xlsx", ".csv"],
            "Presentations": [".ppt", ".pptx"],
            "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"],
            "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
            "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "Code": [".py", ".js", ".java", ".cpp", ".c", ".html", ".css", ".php"],
            "Executables": [".exe", ".msi", ".app", ".deb", ".rpm"],
        }

    def get_category(self, file_extension):
        """Get category for a file extension"""
        file_extension = file_extension.lower()
        for category, extensions in self.categories.items():
            if file_extension in extensions:
                return category
        return "Others"

    def analyze_directory(self):
        """Analyze the directory and show file statistics"""
        file_stats = defaultdict(list)

        for file_path in self.source_dir.iterdir():
            if file_path.is_file():
                extension = file_path.suffix
                category = self.get_category(extension)
                file_stats[category].append(file_path.name)

        print(f"\n=== Analysis of {self.source_dir} ===")

        if not file_stats:
            print("No files found!")
            return file_stats

        for category, files in sorted(file_stats.items()):
            print(f"\n{category} ({len(files)} files):")
            for filename in files[:5]:  # Show first 5
                print(f"  - {filename}")
            if len(files) > 5:
                print(f"  ... and {len(files) - 5} more")

        return file_stats

    def create_demo_files(self):
        """Create demo files for testing"""
        demo_files = [
            "photo1.jpg",
            "photo2.png",
            "document.pdf",
            "report.docx",
            "music.mp3",
            "video.mp4",
            "script.py",
            "data.csv"
        ]
        
        print("Creating demo files...")
        for filename in demo_files:
            filepath = self.source_dir / filename
            filepath.touch()
            print(f"  Created: {filename}")

def main():
    """Demo mode"""
    print("=== File Organizer Demo ===\n")
    
    # Create a demo directory
    demo_dir = Path("demo_organize")
    demo_dir.mkdir(exist_ok=True)
    
    organizer = FileOrganizer(demo_dir)
    
    # Create demo files
    organizer.create_demo_files()
    
    # Analyze directory
    print("\n=== Analyzing Directory ===")
    organizer.analyze_directory()
    
    print("\n=== Demo Complete ===")
    print(f"Demo files created in: {demo_dir.absolute()}")

if __name__ == "__main__":
    main()
