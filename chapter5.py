"""
Chapter 5 Module

This module contains the functions for Chapter 5 of the game,
where the player faces the guardian's challenge and must use their skills to proceed.

# Hikmet Tenis
# 08/17/2024
# Chapter-5

"""
import chapter6

# Define the correct combination codes
CORRECT_CODES = ["1234", "5678", "91011"]

def start_chapter5():
    """Display the introduction for Chapter 5."""
    print("Chapter 5: The Guardian's Challenge")
    start_action_module_ch5()

def start_action_module_ch5():
    """Present the player with action choices for Chapter 5."""
    print("\nChoose an action:")
    print("1. Talk to Hasan about the map")
    print("2. Try combination")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        solve_cipher_option_ch5()
    elif choice == '2':
        try_combination_option()
    else:
        print("Invalid choice, please try again.")
        start_action_module_ch5()

def solve_cipher_option_ch5():
    """Handle the 'Talk to Hasan about the map' action."""
    solve_cipher = input("Do you want to solve the cipher? (yes/no): ")
    
    if solve_cipher.lower() == 'yes':
        show_cipher_puzzle_ch5()
    elif solve_cipher.lower() == 'no':
        start_action_module_ch5()
    else:
        print("Invalid input, please try again.")
        solve_cipher_option_ch5()

def show_cipher_puzzle_ch5():
    """Present the cipher puzzle to the player in Chapter 5."""
    cipher_input = input("Enter the solution to the cipher: ")
    
    if check_cipher_solution_ch5(cipher_input):
        start_chapter6()
    else:
        solve_cipher_option_ch5()

def try_combination_option():
    """Handle the 'Try combination' action."""
    print("You need to enter three correct codes to unlock the door.")
    codes_entered = []

    for i in range(3):
        code = input(f"Enter code {i+1}: ")
        codes_entered.append(code)

    if check_combination_codes(codes_entered):
        print("All codes are correct! The door unlocks.")
        start_chapter6()
    else:
        print("One or more codes were incorrect. Try again.")
        try_combination_option()

def check_combination_codes(codes):
    """Check if all entered codes match the correct combination codes."""
    return codes == CORRECT_CODES

def check_cipher_solution_ch5(solution):
    """Check if the player's solution to the cipher in Chapter 5 is correct."""
    return solution.lower() == "guardianscode"

def start_chapter6():
    """Transition to Chapter 6."""
    print("Chapter 6: The Final Revelation")
    chapter6.start_chapter6()



