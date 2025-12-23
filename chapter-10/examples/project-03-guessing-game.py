#!/usr/bin/env python3
"""
Chapter 10: Python Projects for Beginners
Project 3: Number Guessing Game

An enhanced guessing game with difficulty levels and statistics.
"""

import random
import json
from pathlib import Path

class GuessingGame:
    def __init__(self):
        self.stats_file = "game_stats.json"
        self.stats = self.load_stats()

    def load_stats(self):
        try:
            with open(self.stats_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {
                "games_played": 0,
                "games_won": 0,
                "total_guesses": 0,
                "best_score": None
            }

    def save_stats(self):
        with open(self.stats_file, "w") as file:
            json.dump(self.stats, file, indent=4)

    def show_stats(self):
        print("\n=== Your Statistics ===")
        print(f"Games Played: {self.stats['games_played']}")
        print(f"Games Won: {self.stats['games_won']}")

        if self.stats['games_played'] > 0:
            win_rate = (self.stats['games_won'] / self.stats['games_played']) * 100
            print(f"Win Rate: {win_rate:.1f}%")

            avg_guesses = self.stats['total_guesses'] / self.stats['games_played']
            print(f"Average Guesses per Game: {avg_guesses:.1f}")

        if self.stats['best_score']:
            print(f"Best Score: {self.stats['best_score']} guesses")

    def play_demo(self, difficulty="medium"):
        """Demo mode with pre-set guesses"""
        # Set parameters based on difficulty
        if difficulty == "easy":
            min_num, max_num, max_attempts = 1, 50, 15
        elif difficulty == "medium":
            min_num, max_num, max_attempts = 1, 100, 10
        else:  # hard
            min_num, max_num, max_attempts = 1, 200, 8

        secret_number = random.randint(min_num, max_num)
        
        print(f"\n=== Number Guessing Game ({difficulty.upper()}) ===")
        print(f"Secret number is between {min_num} and {max_num}")
        print(f"Maximum {max_attempts} attempts")
        print(f"(Demo mode: Secret number is {secret_number})")
        
        # Simulate guesses
        demo_guesses = [
            secret_number // 2,  # Too low
            (secret_number + max_num) // 2,  # Might be too high
            secret_number  # Correct!
        ]
        
        attempts = 0
        for guess in demo_guesses:
            if attempts >= max_attempts:
                break
                
            attempts += 1
            print(f"\nAttempt {attempts}/{max_attempts} - Guess: {guess}")
            
            if guess == secret_number:
                print(f"\n🎉 Congratulations! Guessed correctly in {attempts} attempts!")
                
                # Update statistics
                self.stats['games_played'] += 1
                self.stats['games_won'] += 1
                self.stats['total_guesses'] += attempts
                
                if self.stats['best_score'] is None or attempts < self.stats['best_score']:
                    self.stats['best_score'] = attempts
                    print(f"🏆 New best score!")
                
                self.save_stats()
                return True
            elif guess < secret_number:
                print(f"Too low!")
            else:
                print(f"Too high!")
        
        return False

def main():
    """Demo mode"""
    print("=== Guessing Game Demo ===")
    
    game = GuessingGame()
    
    # Play a demo game
    game.play_demo("medium")
    
    # Show statistics
    game.show_stats()
    
    print("\n=== Demo Complete ===")

if __name__ == "__main__":
    main()
