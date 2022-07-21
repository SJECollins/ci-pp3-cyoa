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
    user_choice = input("\n====================================================\
============================\n" + message + "\n").strip().lower()
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
    User can choose to say no, which prints a disappointed message and game
    doesn't start
    """
    global username
    username = input("What's your name? \n").strip().capitalize()
    start_answer = get_user_choice(f"Hello, {username}, do you want to play a game?\
 Yes or No")
    if start_answer == "yes":
        print("Great. To play, enter the letter of your choice in the terminal\
.")
        user_choice = get_user_choice("Ready to start?\n\
A. \033[4mYes\033[0m!\n\
B. Actually, \033[4mno\033[0m, I don't think I want to play after all...")
        if user_choice == "a" or user_choice == "yes":
            clear_terminal()
            start_room()
        elif user_choice == "b" or user_choice == "no":
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
B. Pull the blanket tighter and close your eyes.")
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
B. Sleep harder.")
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
B. Put on your fluffy slippers.")
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
        user_choice = get_user_choice("You feel compelled to:\n\
A. Check inside, though it is as quiet as the rest of the house.\n\
B. Keep going - you don't need to encourage your imagination.")
        if user_choice == "a":
            check_closet()
            break
        elif user_choice == "b":
            continue_hallway()
            break
        else:
            print(f"{user_choice} isn't really an option...\n")


def check_closet():
    """
    Optional. Can collect teddy or golf club.
    User can also back out and pick up nothing
    """
    clear_terminal()
    slowprint("For some reason, you decide to investigate the quiet closet. You \
try to peek through the slats of the closet door, but see nothing except \
darkness. Slowly, you open the closet and peer inside.\n\
As expected, there is only the regular assortment of clutter - coats, shoes, \
golf clubs, your old teddy bear 'Burt'.\n")
    while True:
        user_choice = get_user_choice("You decide to:\n\
A. Take Burt with you, you haven't spent much time together lately.\n\
B. Take a golf club.\n\
C. Take nothing. You don't know why you decided to open the closet in the \
first place.")
        if user_choice == "a":
            pick_ups.append("teddy")
            continue_hallway()
            break
        elif user_choice == "b":
            pick_ups.append("golf_club")
            continue_hallway()
            break
        elif user_choice == "c":
            continue_hallway()
            break
        else:
            print(f"{user_choice} isn't really an option...\n")


def continue_hallway():
    """
    After bedroom or closet. User has option to check bedroom. Can ignore
    """
    clear_terminal()
    if "teddy" in pick_ups:
        slowprint("You take Burt down from the shelf in the closet and grip him \
tightly in your arms.\n")
    elif "golf_club" in pick_ups:
        slowprint("You nod at Burt, but pull a long golf club from the bag in the \
back of the closet. The metal feels cold in your hands.\n")
    slowprint(f"You continue down the hallway and pass the master bedroom on your \
right.\n\
'{username}'\n\
Who said that? You think it came from inside the door. It was so quiet, \
though.\n\
Maybe it was just your mind playing tricks on you?\n")
    while True:
        user_choice = get_user_choice("Will you:\n\
A. Ignore it. It was just the wind.\n\
B. Investigate.")
        if user_choice == "a":
            go_kitchen()
            break
        elif user_choice == "b":
            check_bedroom()
            break
        else:
            print(f"{user_choice} isn't really an option...\n")


def check_bedroom():
    """
    Optional interaction. Leaves master bedroom door open.
    """
    clear_terminal()
    slowprint("Very slowly, you creep across the hall to the door. You press your \
ear up against it, but can hear nothing from inside. The door knob feels cool \
on your hand.\n\
Gingerly, you turn it. The door creaks as you push it open a crack. Peering \
in, the room is so dark you can only see the outline of the duvet on the bed. \
Nothing is stirring in the room. You cannot hear a sound.\n\
Relieved, you leave the door open a crack and continue towards the kitchen.\n")
    global door_open
    if not door_open:
        door_open = True
    time.sleep(3)
    go_kitchen()


def go_kitchen():
    """
    In kitchen. Missable text depending on what items user has
    Choice to use step stool or not
    """
    clear_terminal()
    slowprint("You continue on towards the kitchen. It is as quiet as the rest \
of the house. Moonlight filters in through the windows and illuminates the \
room.\n")
    if "slippers" not in pick_ups:
        if "teddy" in pick_ups:
            slowprint("The tiles feel like ice under your bare feet. You hug Burt \
closely.\n")
        else:
            slowprint("The tiles feel like ice under your bare feet. You shiver and \
hug yourself.\n")
    slowprint("The kettle is tucked right in under the cabinets on the counter\
.\n")
    while True:
        user_choice = get_user_choice("You think:\n\
A. You can reach it if you stretch. \n\
B. There's a stool here somewhere.")
        if user_choice == "a":
            try_reach()
            break
        elif user_choice == "b":
            get_stool()
            break
        else:
            print(f"{user_choice} isn't really an option...\n")


def get_stool():
    """
    Optional function if user decides to get step stool
    """
    clear_terminal()
    slowprint("You think you remember the stool by the backdoor. You walk past \
the island in the middle of the kitchen, past the table and find the stool \
next to the door, beside your wellies.\n\
You glance at the door quickly as you retrieve the stool. It looks locked to \
you. Of course it is.\n\
You bring the stool back over to the counter and step up on it. You can \
easily pull the kettle out from under the cabinet.\n")
    global stool_out
    stool_out = True
    time.sleep(3)
    kettle_on()


def try_reach():
    """
    Optional function if user decides to ignore step stool.
    Will lose current item. Except slippers
    """
    clear_terminal()
    slowprint("You think your arms are long enough. The counter is a little wide, \
though.\n")
    if "teddy" in pick_ups:
        pick_ups.remove("teddy")
        slowprint("So, you pop Burt on the counter to free your hands.\n")
    elif "golf_club" in pick_ups:
        pick_ups.remove("golf_club")
        slowprint("So, you place the golf club down to free your hands.\n")
    slowprint("On your toes, leaning on the counter with one hand, you reach out for \
the kettle. You can just about pull it out from under the cabinet.\n")
    time.sleep(3)
    kettle_on()


def kettle_on():
    """
    Turn kettle on. No user interaction.
    Missable text depending on if user got the stool
    """
    clear_terminal()
    slowprint("You flick the switch on the kettle and the little light above it comes \
on. It starts a low rumble. While the kettle boils, you collect your \
ingredients.\n\
Your favourite mug is sitting on the edge of the sink where you left it that \
afternoon. You collect it.\n\
The tea bags and sugar are much easier to reach than the kettle. You place a \
tea bag in your mug. You take a spoon from the drawer and place it next to \
your cup.\n")
    time.sleep(3)
    slowprint("You walk over to the fridge to get the milk. You open the door and \
take out the milk carton. As the fridge door closes, you can see the back door\
. It is slightly open.\n")
    if stool_out:
        slowprint("But, it was just closed?\n")
    else:
        slowprint("Was that open before?\n")
    time.sleep(3)
    shadow_appears()


def shadow_appears():
    """
    Monster. User can choose to run or do nothing
    """
    slowprint("As you watch, the back door slowly creaks open. A shadowy figure forms \
before your. The hair stands up on the back of your neck as it approaches.\n\
It seems to glide across the floor without taking a step.\n")
    while True:
        user_choice = get_user_choice("You:\n\
A. Run.\n\
B. Freeze.")
        if user_choice == "a":
            run_away()
            break
        elif user_choice == "b":
            you_freeze()
            break
        else:
            print(f"{user_choice} is not an option.\n")


def you_freeze():
    """
    User chooses freeze. Has another chance do make a choice
    """
    clear_terminal()
    slowprint(f"'{username},' the shadowy figure whispers.\n\
How does it know your name?\n")
    while True:
        user_choice = get_user_choice("You:\n\
A. Call for help.\n\
B. Run.")
        if user_choice == "a":
            kitchen_cry()
            break
        elif user_choice == "b":
            run_away()
            break
        else:
            print(f"{user_choice} is REALLY not an option.\n")


def kitchen_cry():
    """
    User calls for help. If has teddy, can survive. Else dies
    """
    clear_terminal()
    if "teddy" in pick_ups:
        slowprint("You open your mouth, but then in a panic you toss Burt at the \
figure. The shadow stops and catches him. While it's distracted, you make a \
break for it.\n")
        pick_ups.remove("teddy")
        time.sleep(3)
        run_away()
    elif "golf_club" in pick_ups:
        slowprint("The figure reaches for you. Impulsively, you swing the golf club \
that is still in your hands. You miss and the shadow continues to advance...\n\
")
        time.sleep(3)
    user_dies()


def user_dies():
    """
    Reusable death end game
    """
    slowprint(f"You open your mouth to cry out for help, but your voice stops in \
your throat.\n\
'{username},' the figure groans.\n\
It reaches for you.\n\
Your legs quiver. Your feet refuse to listen to you. Your eyes widen but your \
vision fades. You can feel a weight press down upon you...\n")
    time.sleep(3)
    slowprint(f"You are overcome with darkness. All you feel and see and hear is \
nothingness.\n\
'Goodnight, {username}.'\n\
You never wake up again.\n\
The end!\n")
    return


def run_away():
    """
    User chooses to run away. If took stool out, can delay shadow
    If has slippers on and stool out, can die unless has teddy
    """
    clear_terminal()
    slowprint(f"You turn and run.\n\
'{username},' the figure growls.\n")
    if stool_out and "slippers" in pick_ups:
        slowprint("You run through the kitchen and hop over the stool as you go. As \
you leap, the bunny ears of your fluffy slippers catch on the stool and \
you fall! You collapse on the kitchen tiles and the shadow looms over you.\n")
        if "teddy" in pick_ups:
            slowprint("In a panic, you throw Burt at the shadowy figure. It catches \
him. As it seems to stare at Burt in confusion, you kick your slippers off \
and run for the hallway.\n")
            time.sleep(3)
            run_hallway()
        else:
            user_dies()
    elif stool_out:
        slowprint("You run through the kitchen, hopping over the stool as you go. The \
figure follows, but as you reach the hallway, you glance back and see it \
stumble over your step stool and fall on the kitchen tiles.\n")
        time.sleep(3)
        global shadow_delayed
        if not shadow_delayed:
            shadow_delayed = True
            run_hallway()
    elif not stool_out:
        run_hallway()


def run_hallway():
    """
    Run to hallway. User has choice of four rooms. 2 could have been changed
    by previous decisions. Time to escape effected by if shadow delayed
    """
    clear_terminal()
    if not shadow_delayed:
        slowprint("You reach the hallway, but the shadow is right on your heels. \
There's little time.\n")
    elif shadow_delayed:
        slowprint("You reach the hallway before the shadowy figure can gather \
itself.\n")
    slowprint("You have to hide.\n")
    while True:
        user_choice = get_user_choice("You run to:\n\
A. The master bedroom.\n\
B. The closet.\n\
C. Your bedroom.\n\
D. The front door.")
        if user_choice == "a":
            hide_master()
            break
        elif user_choice == "b":
            hide_closet()
            break
        elif user_choice == "c":
            hide_bedroom()
            break
        elif user_choice == "d":
            front_door()
            break
        else:
            print(f"{user_choice} is REALLY not an option now!\n")


def front_door():
    """
    Front door. User dies unless has teddy still.
    If has teddy, runs to bedroom
    """
    clear_terminal()
    slowprint(f"You race for the front door, hoping to escape from the house.\
You pull on the handle. The door won't budge.\n\
'{username},' whispers the shadowy figure as it approaches.\n\
You fumble with the door and, too late, realise the bolt at the top is \
locked, out of reach.\n")
    if "teddy" in pick_ups:
        slowprint("In a panic, you throw Burt at the shadowy figure. It catches \
him. As it seems to stare at Burt in confusion, you run for your bedroom.\n")
        pick_ups.remove("teddy")
        hide_bedroom()
    else:
        time.sleep(3)
        user_dies()


def hide_closet():
    """
    Hide in closet. User dies if shadow right behind, obviously.
    """
    clear_terminal()
    slowprint("You race for the closet, diving through the slatted doors \
and pulling them closed behind you. Hastily, you cover yourself in a \
pile of winter coats. You put your hand to your mouth and try to stay \
as quiet as you can.\n\
All you can hear is your own breathing.\n")
    if not shadow_delayed:
        slowprint("Only seconds pass before the closet door slowly opens.\n")
        time.sleep(3)
        hidden_user_dies()
    elif shadow_delayed:
        time.sleep(3)
        user_hides()


def user_hides():
    """
    Reusable hiding for closet, master bedroom while shadow delayed
    User always runs to own bedroom
    """
    slowprint("An eternity passes as you hide in the darkness. Is it still out \
there?\n\
You think you hear something pass by the door, but did you just imagine \
that?\n\
How much longer can you wait?\n\
You think you can hear a sound coming from the kitchen.")
    while True:
        user_choice = get_user_choice("You decide to:\n\
A. Run to your bedroom.\n\
B. Stay hidden.")
        if user_choice == "a":
            hide_bedroom()
            break
        elif user_choice == "b":
            hidden_user_dies()
            break
        else:
            print(f"{user_choice} is not an option!\n")


def hidden_user_dies():
    """
    Reusable death end game when user hidden
    Two lines added for variation, then calls user_dies function
    """
    slowprint("You stay frozen in fear where you are.\n\
A cold chill runs up your spine and, suddenly, you see it before you.\n")
    user_dies()


def hide_master():
    """
    Hide in master bedroom. If user previously interacted, door open.
    If shadow delayed, can hide. If not delayed, caught.
    If not interacted before, door closed. If shadow delayed, can go
    elsewhere. If not delayed, caught
    """
    clear_terminal()
    slowprint("The master bedroom is closest so you race for the door.\n")
    if shadow_delayed and door_open:
        slowprint("You slip through the open door.\n\
Expecting safety, you realise the mound of blankets you saw earlier \
is just that - blankets. The room is empty. You have no time to wonder \
why, so you dive underneath the bed.\n")
        time.sleep(3)
        user_hides()
    elif shadow_delayed and not door_open:
        slowprint("You turn the doorknob, but the door won't open. It's locked? \
Why?\n")
        while True:
            user_choice = get_user_choice("You turn around and:\n\
A. Run to your bedroom.\n\
B. Run to the closet.")
            if user_choice == "a":
                hide_bedroom()
                break
            if user_choice == "b":
                hide_closet()
                break
            else:
                print(f"{user_choice} is REALLY not an option now!\n")
    elif not shadow_delayed:
        slowprint("You almost reach the door, but the shadowy figure is right \
behind you.\n")
        user_dies()


def hide_bedroom():
    """
    Back to own room. 3 options to escape.
    Under covers, with teddy, only happy ending.
    Under bed, caught
    Can go to window
    """
    clear_terminal()
    slowprint("You race into your bedroom. As quickly and quietly as you can, \
you close the door behind you. What now?\n")
    while True:
        user_choice = get_user_choice("You:\n\
A. Slide under your bed.\n\
B. Run to the window.\n\
C. Jump back into bed and pull the covers over your head.")
        if user_choice == "a":
            under_bed()
            break
        elif user_choice == "b":
            run_window()
            break
        elif user_choice == "c":
            back_bed()
            break
        else:
            print(f"{user_choice} is not an option!\n")


def under_bed():
    """
    Hiding under bed. Gets caught always
    """
    clear_terminal()
    slowprint(f"You dive head first under your bed and curl yourself into as \
small of a ball as you can.\n\
You cover your mouth and try to quiet your breathing.\n\
'{username}.'\n\
The bedroom door creaks open slowly.\n")
    time.sleep(3)
    hidden_user_dies()


def run_window():
    """
    If window still open or has golf club, can escape.
    If window closed and no golf club, caught.
    """
    clear_terminal()
    if window_closed:
        if "golf_club" in pick_ups:
            slowprint(f"You run over to the window and try to slide it open, but \
it's jammed. You can't force it.\n\
The golf club! You still have it!\n\
You can hear the door slowly open behind you.\n\
'{username},' the shadow softly growls.\n\
You swing the club.\n")
            time.sleep(3)
            escape_house()
        else:
            slowprint("You run over to the window and try to slide it open. It's \
jammed. Pushing with all your strength, you can't force it open.\n\
You turn as the bedroom door slowly opens and try to make yourself as small \
as you can in the corner of the room.\n")
            time.sleep(3)
            user_dies()
    elif not window_closed:
        slowprint(f"You run over to the window. It's still open a crack. You slide \
it open even wider as you hear your bedroom door slowly open behind you.\n\
'{username},' the shadow softly growls.\n")
        escape_house()


def escape_house():
    """
    Ending - survives?
    """
    clear_terminal()
    slowprint("You slip out your bedroom window and run out on to the footpath. \
Looking back at your house, you think you see the shadow in your window.\n\
It's quiet out. The road is still. There are no lights in any of the houses.\n\
Your grandparents live nearby. You go there every Sunday, it's not a very \
long drive.\n\
You think you know which way to go. It'll be safe there.\n\
You start walking.\n\
The end!\n")


def back_bed():
    """
    Under covers. If have teddy, can win.
    Otherwise, dies
    """
    clear_terminal()
    slowprint("You dive into your bed and pull the covers up over your head. You \
close your eyes and try as hard as you can to fall back to sleep.\n")
    if "teddy" in pick_ups:
        slowprint("You hug Burt close.\n")
        time.sleep(3)
        wake_win()
    else:
        slowprint("You can hear it. The bedroom creaks open. You lift the edge of \
your blankets and peek out with one eye.\n")
        time.sleep(3)
        hidden_user_dies()


def wake_win():
    """
    Happy ending!
    """
    slowprint(f"'{username}, why is there milk all over the kitchen floor?'\n\
Your eyes open. Light seeps in around your blankets. You throw them back.\n\
It's morning. Your bedroom is bright and empty. There's no shadowy figures \
lurking in the corners.\n\
It must have all been a terrible nightmare.\n\
You're safe.\n\
You look at Burt, still cradled in your arms.\n\
The end!\n")


main()
