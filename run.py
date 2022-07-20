"""
Imports
"""
import os
import sys
import time


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


def slowprint(text):
    """
    Prints text with delay between letters.
    Code from replit, link in credits in readme.
    """
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


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
            clear_terminal()
            start_room()
        else:
            print(f"That's too bad, {username}")
    else:
        print(f"Well, alright {username}. Maybe next time...")


def start_room():
    """
    Starting room. Choice to get up or go back to sleep
    """
    clear_terminal()
    slowprint("You slowly open your eyes to find yourself safely in your own bed\
. At first the room seems pitch black, except for the light from the clock on\
 your bedside table. It reads: 02:00.\n\
You don't know why, but you feel wide awake and your heart is beating hard.\n")
    while True:
        user_choice = get_user_choice("Will you:\n\
A. Get up and make a cup of tea.\n\
B. Try to go back to sleep.")
        if user_choice == "a":
            get_up()
            break
        elif user_choice == "b":
            try_sleep()
            break
        else:
            print(f"{user_choice} isn't really an option...\n")


def try_sleep():
    """
    Try to go back to sleep. Choice to get up or keep trying to sleep
    """
    clear_terminal()
    slowprint("You have to get up for school early in the morning. So, you roll \
over in your bed and pull the covers up over your head. After a few moments \
of silence, you hear a soft rustling.\n\
Very slowly, you peek out from under your covers. In the darkness, you spy the\
 window open a crack. A light breeze is moving the curtains.\n")
    while True:
        user_choice = get_user_choice("It's chilly in your room, so you:\n\
A. Get up.\n\
B. Pull the blanket tighter and close your eyes.\n")
        if user_choice == "a":
            get_up()
            break
        elif user_choice == "b":
            blanket_tighter()
            break
        else:
            print(f"{user_choice} isn't really an option...\n")


def blanket_tighter():
    """
    Blankets tighter. Final chance to get up
    """
    clear_terminal()
    slowprint(f"You pull the blanket back over your head and squeeze your eyes \
shut.\n\
'{username}'\n\
You think you hear a voice softly calling your name. You're not sure where \
it's coming from, or even if you really heard it.\n")
    while True:
        user_choice = get_user_choice("You decide to:\n\
A. Investigate.\n\
B. Sleep harder.\n")
        if user_choice == "a":
            get_up()
            break
        elif user_choice == "b":
            sleep_harder()
            break
        else:
            print(f"{user_choice} isn't really an option...\n")


def sleep_harder():
    """
    Sleep harder. First game end.
    """
    clear_terminal()
    slowprint("You really do have to get up early and you've never been a very \
inquisitive person. You pull the blanket tight around your ears and scrunch \
your eyes even tighter. As you do, you feel a chill run up the back of your \
neck and the blanket starts to feel very heavy...\n")
    time.sleep(3)
    slowprint(f"\n'{username}'\n\
Who's saying that? You try to open your eyes and peek out from the covers, but\
 your eyelids won't open and the covers are weighing you down...\n")
    time.sleep(3)
    slowprint("\nThe covers press harder and harder and your eyelids squeeze \
tighter and tighter until all you feel is pressure and all you see is \
nothingness.\n\
You never wake up again.\n\
The end!\n")
    return


def get_up():
    """
    Get up.
    Choice to close window or get slippers. Either changes window_closed
    boolean or appends slippers to our pick_ups list.
    Calls leave_bedroom function either way after user decision
    """
    clear_terminal()
    slowprint("Maybe a cup of tea will help you drift off to sleep. You climb\
 out of bed. The window is slightly open, letting a cold breeze into the \
house. At the end of your bed are an oversized pair of fluffy bunny slippers.\
\n")
    while True:
        user_choice = get_user_choice("You shiver and:\n\
A. Close the window.\n\
B. Put on your fluffy slippers.\n")
        if user_choice == "a":
            global window_closed
            if not window_closed:
                window_closed = True
            break
        elif user_choice == "b":
            pick_ups.append("slippers")
            break
        else:
            print(f"{user_choice} isn't really an option...\n")

    leave_bedroom()


def leave_bedroom():
    """
    Leave bedroom.
    First line depends on choice in get_up function
    Choice to investigate closet. Optional - user can ignore
    """
    clear_terminal()
    if window_closed:
        slowprint("You slide the window closed and shuffle out into the hallway \
in your bare feet.\n")
    else:
        slowprint("You shiver and slip your slippers on, then shuffle out into \
the hallway.\n")
    slowprint("The house is still. You cannot hear a sound. You creep along the \
hallway as quietly as you can. As you go, on your left you pass the hallway \
closet.\n")
    while True:
        user_choice = input("You feel compelled to:\n\
A. Check inside, though it is as quiet as the rest of the house.\n\
B. Keep going - you don't need to encourage your imagination.\n\
")
        if user_choice == "a":
            # check_closet()
            break
        elif user_choice == "b":
            # continue_hallway()
            break
        else:
            print(f"{user_choice} isn't really an option...\n")


main()
