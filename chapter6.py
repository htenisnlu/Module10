"""
Chapter 6 Module

This module contains the functions for Chapter 6 of the game,
which is the final chapter where the player faces the ultimate challenge.

# Hikmet Tenis
# 08/17/2024
# Chapter-6

"""

def start_chapter6():
    """Begin Chapter 6 of the game."""
    print("Chapter 6: The Final Challenge")
    show_chapter6_intro()

def show_chapter6_intro():
    """Display the introduction for Chapter 6."""
    print("You have reached the final chapter. The Golden Scarab awaits...")
    start_action_module_ch6()

def start_action_module_ch6():
    """Present the player with action choices for Chapter 6."""
    print("\nChoose an action:")
    print("1. Use the whip to reach the Golden Scarab")
    print("2. Try jumping across to the Golden Scarab")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        use_whip()
    elif choice == '2':
        try_jumping()
    else:
        print("Invalid choice, please try again.")
        start_action_module_ch6()

def use_whip():
    """Handle the 'Use the whip' action."""
    print("You skillfully use your whip to reach the Golden Scarab.")
    end_game()

def try_jumping():
    """Handle the 'Try jumping' action."""
    print("You decide to try jumping across...")
    game_over()

def end_game():
    """End the game with a successful conclusion."""
    print("Congratulations! You have successfully completed the adventure and obtained the Golden Scarab.")
    print("The game shows the end of the game cinematics.")

def game_over():
    """End the game with a game over."""
    print("Game Over.")
    print("Unfortunately, you didn't survive the final challenge. Better luck next time!")

