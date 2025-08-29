"""
ATM Simulator Main Program
Author: ATM Development Team
Date: August 2025

This is the main entry point for the ATM simulator application.
It handles the overall program flow and user interaction.
"""

from modules.authentication import login_user
from modules.atm_operations import ATMOperations
from modules.gui_interface import run_gui, ATMInterface
from modules.database import initialize_sample_data
import sys


def main():
    """
    Main function that controls the ATM simulator flow.
    
    This function:
    1. Initializes the system
    2. Handles user login
    3. Runs the GUI application
    """
    # Initialize sample data and run GUI directly
    accounts = initialize_sample_data()
    run_gui(accounts)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Critical error: {e}")
        print("Program terminated. Please contact support.")
        sys.exit(1)
