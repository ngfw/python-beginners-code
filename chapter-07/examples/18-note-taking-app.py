#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 18: Simple Note-Taking App (Practical Project)

A complete note-taking application with JSON persistence.
This demonstrates a practical file I/O project.
"""

import json
import datetime

class NoteApp:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        """Load notes from file"""
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_notes(self):
        """Save notes to file"""
        with open(self.filename, "w") as file:
            json.dump(self.notes, file, indent=4)

    def add_note(self, title, content):
        """Add a new note"""
        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "content": content,
            "created": datetime.datetime.now().isoformat()
        }
        self.notes.append(note)
        self.save_notes()
        print(f"Note '{title}' added!")

    def list_notes(self):
        """List all notes"""
        if not self.notes:
            print("No notes yet!")
            return

        for note in self.notes:
            print(f"\n[{note['id']}] {note['title']}")
            print(f"Created: {note['created']}")
            print(f"{note['content'][:50]}...")  # First 50 chars

    def view_note(self, note_id):
        """View a specific note"""
        for note in self.notes:
            if note['id'] == note_id:
                print(f"\nTitle: {note['title']}")
                print(f"Created: {note['created']}")
                print(f"\n{note['content']}")
                return
        print("Note not found!")

    def delete_note(self, note_id):
        """Delete a note"""
        self.notes = [n for n in self.notes if n['id'] != note_id]
        self.save_notes()
        print(f"Note {note_id} deleted!")

def main():
    """Main function - demo mode"""
    app = NoteApp()
    
    print("=== Note App Demo ===\n")
    
    # Add some notes
    print("Adding notes...")
    app.add_note("Python Basics", "Python is an amazing language for beginners")
    app.add_note("File I/O", "Learned how to read and write files today")
    
    # List notes
    print("\n=== Listing all notes ===")
    app.list_notes()
    
    # View a specific note
    print("\n=== Viewing note #1 ===")
    app.view_note(1)
    
    print("\n=== Demo complete! ===")

if __name__ == "__main__":
    main()
