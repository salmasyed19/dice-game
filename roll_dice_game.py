# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 15:45:25 2023

@author: Syed Salma
"""

import random

def roll_dice():
    min_value = 1
    max_value = 6
    
    while True:
        # Generate a random number between 1 and 6 (inclusive)
        dice_roll = random.randint(min_value, max_value)
        
        print(f"You rolled a {dice_roll}.")
        
        # Ask if the player wants to roll again
        roll_again = input("Do you want to roll again? (yes/no): ").lower()
        
        if roll_again != 'yes' and roll_again != 'y':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    roll_dice()
y