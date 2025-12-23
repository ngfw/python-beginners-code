#!/usr/bin/env python3
"""
Chapter 7: File I/O
Example 15: Save App Settings (JSON Class)

Demonstrates a Settings class for managing app configuration.
"""

import json

class Settings:
    def __init__(self, filename="settings.json"):
        self.filename = filename
        self.settings = self.load()

    def load(self):
        """Load settings from file or return defaults"""
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {
                "theme": "dark",
                "language": "en",
                "notifications": True
            }

    def save(self):
        """Save settings to file"""
        with open(self.filename, "w") as file:
            json.dump(self.settings, file, indent=4)

    def get(self, key):
        """Get a setting value"""
        return self.settings.get(key)

    def set(self, key, value):
        """Set a setting value and save"""
        self.settings[key] = value
        self.save()

# Usage
print("=== Settings Manager Demo ===")
settings = Settings()
print(f"Current theme: {settings.get('theme')}")  # dark

print("\n=== Changing settings ===")
settings.set("theme", "light")
settings.set("language", "fr")
print(f"New theme: {settings.get('theme')}")  # light

# Load again to verify persistence
print("\n=== Reloading settings ===")
settings2 = Settings()
print(f"Theme after reload: {settings2.get('theme')}")  # light
print(f"Language after reload: {settings2.get('language')}")  # fr
