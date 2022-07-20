"""
Imports
"""
import os


# Variables and objects
username = ""
pick_ups = []
window_closed = False
door_open = False
stool_out = False
shadow_delayed = False


def get_user_choice(message):
    """
    Function to take input from user
    """
    user_choice = input("\n**--------------------------------------------------\
--------------------------**\n" + message + "\n").strip().lower()
    return user_choice


def clear_terminal():
    """
    Function to clear terminal
    """
    os.system("clear")


def main():
    """
    Starting function. Updates username. Prompts user to begin story.
    User can choose to say no, which prints a disappointed message and game \
    doesn't start

    """
    global username
    username = input("What's your name? \n").strip().capitalize()
    start_answer = get_user_choice(f"Hello, {username}, do you want to play a game?\
 Yes or No\n")
    if start_answer == "yes":
        print("Great. To play, enter the letter of your choice in the terminal\
.")
        user_choice = get_user_choice("Ready to start?\n\
A. Yes!\n\
B. Actually, I don't think I want to play after all...\n")
        if user_choice == "a":
            print("Start")
            # clear_terminal()
            # start_room()
        else:
            print(f"That's too bad, {username}")
    else:
        print(f"Well, alright {username}. Maybe next time...")


main()
