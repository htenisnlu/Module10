"""
Chapter 3 Module

This module contains the functions for Chapter 3 of the game,
where the player faces increasing challenges and must make critical decisions.

# Hikmet Tenis
# 08/17/2024
# Chapter-3

"""
import chapter4
import chapter5
def start_chapter3():
    """Begin Chapter 3 of the game."""
    print("Chapter 3: The Conflict Begins")
    show_chapter3_intro()

def show_chapter3_intro():
    """Display the introduction for Chapter 3."""
    print("The tension builds as you face new challenges.")
    start_action_module_ch3()

def start_action_module_ch3():
    """Present the player with action choices for Chapter 3."""
    print("\nChoose an action:")
    print("1. Go to Hotel")
    print("2. Fight")
    print("3. Run Away")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        rest_module()
    elif choice == '2':
        fight_module()
    elif choice == '3':
        chapter5.start_chapter5()
    else:
        print("Invalid choice, please try again.")
        start_action_module_ch3()

def rest_module():
    """Handle the 'Go to Hotel' action."""
    print("You take a rest at the hotel.")
    start_action_module_ch3()

def fight_module():
    """Handle the 'Fight' action."""
    fight_outcome = input("Did you win the fight? (yes/no): ")
    
    if fight_outcome.lower() == 'yes':
        print("You won the fight and proceed confidently!")
        start_chapter4()
    elif fight_outcome.lower() == 'no':
        print("You lost, but Professor Hasan saves you.")
        start_chapter4()
    else:
        print("Invalid input, please try again.")
        fight_module()

def start_chapter4():
    """Transition to Chapter 4."""
    print("Chapter 4: A New Discovery")
    chapter4.start_chapter4()

