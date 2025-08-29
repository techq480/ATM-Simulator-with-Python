"""
User Interface Module
Handles all user interface elements including menus, prompts, and input collection.
"""

import getpass
import sys


def display_welcome():
    """
    Display welcome banner and system information.
    """
    print("\n" + "="*60)
    print("                  🏦 WELCOME TO ATM 🏦")
    print("                   Secure Banking System")
    print("="*60)
    print("📍 Location: Main Branch ATM")
    print("🕒 Available 24/7")
    print("🔒 Secure & Encrypted")
    print("="*60)


def display_menu():
    """
    Display main ATM menu options.
    """
    print("\n" + "="*50)
    print("               🏧 ATM MAIN MENU 🏧")
    print("="*50)
    print("1. 💰 View Balance")
    print("2. 💵 Deposit Money")
    print("3. 💸 Withdraw Money")
    print("4. 🔐 Change PIN")
    print("5. 📄 Mini Statement (Last 5 Transactions)")
    print("6. 🚪 Exit")
    print("="*50)


def get_user_input(prompt, mask=False):
    """
    Get user input with optional masking for sensitive data.
    
    Args:
        prompt (str): Prompt message to display
        mask (bool): Whether to mask input (for PINs)
        
    Returns:
        str: User input
    """
    try:
        if mask:
            return getpass.getpass(prompt)
        else:
            return input(prompt)
    except KeyboardInterrupt:
        print("\n\n⚠️ Operation cancelled by user.")
        return ""
    except EOFError:
        print("\n\n⚠️ Input terminated.")
        return ""


def get_user_choice(prompt):
    """
    Get user menu choice with input validation prompt.
    
    Args:
        prompt (str): Prompt message for menu selection
        
    Returns:
        str: User's menu choice
    """
    return get_user_input(prompt).strip()


def display_error(message):
    """
    Display error message in a consistent format.
    
    Args:
        message (str): Error message to display
    """
    print(f"❌ {message}")


def display_success(message):
    """
    Display success message in a consistent format.
    
    Args:
        message (str): Success message to display
    """
    print(f"✅ {message}")


def display_info(message):
    """
    Display information message in a consistent format.
    
    Args:
        message (str): Information message to display
    """
    print(f"ℹ️ {message}")


def display_warning(message):
    """
    Display warning message in a consistent format.
    
    Args:
        message (str): Warning message to display
    """
    print(f"⚠️ {message}")


def confirm_action(message):
    """
    Ask user for confirmation before proceeding with an action.
    
    Args:
        message (str): Confirmation message
        
    Returns:
        bool: True if user confirms, False otherwise
    """
    while True:
        response = get_user_input(f"{message} (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            display_error("Please enter 'y' for yes or 'n' for no.")


def clear_screen():
    """
    Clear the terminal screen (platform independent).
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def pause_for_user():
    """
    Pause execution and wait for user to press Enter.
    """
    try:
        input("\nPress Enter to continue...")
    except KeyboardInterrupt:
        pass