"""
Chapter 1 Module

# Hikmet Tenis
# 08/17/2024
# Chapter-1

This module contains the functions for Chapter 1 of the game,
including the game's initial setup and the first major decisions.
"""
from professor import Professor
import chapter2
def start_game():
    """Initialize the game and prompt the user for their username."""
    print("Welcome to the Game!")
    prompt_username()

def prompt_username():
    """Prompt the player to enter their username."""
    username = input("Please enter your username: ")
    professor = Professor(name=username, weapons=["whip", "revolver"])
    print(professor.introduce())
    show_intro()

def show_intro():
    """Display the game's introduction and start Chapter 1."""
    print("Welcome to the adventure!")
    input("Press any key to start...")
    start_chapter1()

def start_chapter1():
    """Begin Chapter 1 of the game."""
    print("Chapter 1: The Beginning")
    print("You find yourself in a mysterious situation...")
    start_action_module()

def start_action_module():
    """Present the player with action choices for Chapter 1."""
    print("\nChoose an action:")
    print("1. Translate Tablet")
    print("2. Call James about the tablet")
    print("3. Talk to Police")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        translate_module()
    elif choice == '2':
        call_module()
    elif choice == '3':
        talk_module()
    else:
        print("Invalid choice, please try again.")
        start_action_module()

def translate_module():
    """Handle the 'Translate Tablet' action."""
    print("You found a hidden map in the tablet!")
    travel_decision()

def call_module():
    """Handle the 'Call James' action."""
    print("You called James, but he seems to be acting weird...")
    start_action_module()

def talk_module():
    """Handle the 'Talk to Police' action."""
    print("You talked to the police about your situation and give them his statement, meanwhile he gets to know more about the stranger.  (finds out that stranger has traveled from Egypt to talk to him)")
    travel_decision()

def travel_decision():
    """Ask the player if they want to travel to Egypt."""
    print("Do you want to travel to Egypt?")
    decision = input("Enter 'yes' to travel, or 'no' to stay: ")
    
    if decision.lower() == 'yes':
        start_chapter2()
    elif decision.lower() == 'no':
        print("You decided to stay and investigate further.")
        start_action_module()
    else:
        print("Invalid input, please try again.")
        travel_decision()

def start_chapter2():
    """Transition to Chapter 2."""
    print("Chapter 2: The Journey to Egypt")
    print("Your adventure continues as you arrive in Egypt...")
    chapter2.start_chapter2()

