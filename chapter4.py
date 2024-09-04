"""
Chapter 4 Module

This module contains the functions for Chapter 4 of the game,
where the player delves deeper into the mysteries and faces more complex puzzles.

# Hikmet Tenis
# 08/17/2024
# Chapter-4

"""
import chapter6
import chapter5
def start_chapter4():
    """Display the introduction for Chapter 4."""
    print("Chapter 4: The Mystery Deepens")
    start_action_module_ch4()

def start_action_module_ch4():
    """Present the player with action choices for Chapter 4."""
    print("\nChoose an action:")
    print("1. Talk to Hasan about the map")
    print("2. Enter the Pyramid")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        solve_cipher_option()
    elif choice == '2':
        solve_puzzle_option()
    else:
        print("Invalid choice, please try again.")
        start_action_module_ch4()

def solve_cipher_option():
    """Handle the 'Talk to Hasan about the map' action."""
    print("If Professor solves the complicated cipher and read the map, map will lead them to secret entrance)")
    solve_cipher = input("Do you want to solve the cipher? (yes/no): ")
    
    if solve_cipher.lower() == 'yes':
        show_cipher_puzzle()
    elif solve_cipher.lower() == 'no':
        start_action_module_ch4()
    else:
        print("Invalid input, please try again.")
        solve_cipher_option()

def solve_puzzle_option():
    """Handle the 'Enter the Pyramid' action."""
    solve_puzzle = input("Do you want to solve the puzzle? (yes/no): ")
    
    if solve_puzzle.lower() == 'yes':
        show_pyramid_puzzle()
    elif solve_puzzle.lower() == 'no':
        start_chapter5()
    else:
        print("Invalid input, please try again.")
        solve_puzzle_option()

def show_cipher_puzzle():
    """Present the cipher puzzle to the player."""
    cipher_input = input("Enter the solution to the cipher: ")
    
    if check_cipher_solution(cipher_input):
        print("Congrats...!!!, you entered the correct code.!!!")
        start_chapter6()
    else:
        print("Wrong code, try again.!!!")
        solve_cipher_option()

def show_pyramid_puzzle():
    """Present the pyramid puzzle to the player."""
    puzzle_input = input("Enter the solution to the puzzle: ")
    
    if check_puzzle_solution(puzzle_input):
        print("Congrats...!!!, you entered the correct code.!!!")
        start_chapter6()
    else:
        print("Wrong code, try again.!!!")
        solve_puzzle_option()

def check_cipher_solution(solution):
    """Check if the player's solution to the cipher is correct."""
    return solution.lower() == "ancientcode"

def check_puzzle_solution(solution):
    """Check if the player's solution to the pyramid puzzle is correct."""
    return solution == "1234"

def start_chapter5():
    """Transition to Chapter 5."""
    print("Chapter 5: The Unexpected Journey")
    chapter5.start_chapter5()

def start_chapter6():
    """Transition to Chapter 6."""
    print("Chapter 6: The Finishing the Journey")
    chapter6.start_chapter6()