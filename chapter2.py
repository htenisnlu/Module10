"""
Chapter 2 Module

This module contains the functions for Chapter 2 of the game,
continuing the player's journey in Egypt with more choices and challenges.

# Hikmet Tenis
# 08/17/2024
# Chapter-2

"""
import chapter3
def start_chapter2():
    """Begin Chapter 2 of the game."""
    print("Chapter 2: The Journey Continues")
    print("You have arrived in Egypt.")
    show_chapter2_intro()

def show_chapter2_intro():
    """Display the introduction for Chapter 2."""
    print("As you arrive in Egypt, the mystery deepens...")
    start_action_module_ch2()

def start_action_module_ch2():
    """Present the player with action choices for Chapter 2."""
    print("\nChoose an action:")
    print("1. Go to Hotel")
    print("2. Call Hasan")
    print("3. Go to Giza")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        go_to_hotel()
    elif choice == '2':
        call_hasan()
    elif choice == '3':
        go_to_giza()
    else:
        print("Invalid choice, please try again.")
        start_action_module_ch2()

def go_to_hotel():
    """Handle the 'Go to Hotel' action."""
    print("You decided to rest at the hotel.")
    start_action_module_ch2()

def call_hasan():
    """Handle the 'Call Hasan' action."""
    print("You called Hasan and discussed your plans.")
    print("No answer and he get a strange email from Hasan telling Professor to be careful, and he also asks him to meet with him at Pyramid Giza. Hmm, that’s weird he thinks")
    start_action_module_ch2()

def go_to_giza():
    """Handle the 'Go to Giza' action."""
    print("You decided to visit the Pyramid at Giza.")
    start_chapter3()

def start_chapter3():
    """Transition to Chapter 3."""
    chapter3.start_chapter3()

