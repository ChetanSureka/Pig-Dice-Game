import random

PLAYER_SCORE = 0
COMPUTER_SCORE = 0

def roll():
    die_val = random.randint(1,6)
    return die_val

def hold(current_scr, current_player):
    total_scr = current_scr
    global PLAYER_SCORE, COMPUTER_SCORE
    if current_player == "player":
        print("\n\t\t\tYour score: ", total_scr)
        if total_scr >= 20:
            print("YOU WIN !!!\n\nGame Over")
        else:
            PLAYER_SCORE = total_scr
            print("The die is passed on to the computer.")
            set_current_player_to("computer")
            
    elif current_player == "computer":
        print("\n\n\t\t\tComputer score: ", total_scr)
        if total_scr >= 20:
            print("I WON !!!\n\nGame Over")
        else:
            COMPUTER_SCORE = total_scr
            print("The die is passed on to the next player.")
            set_current_player_to("player")

def gui():
    print("\nSelect any one option:\n1. Roll\n2. Hold")
    player_decision = int(input("Enter your choice: "))
    return player_decision

def comp_dec_hold():
    decision = random.randint(1,2)
    return decision

def set_current_player_to(player):
    global COMPUTER_SCORE, PLAYER_SCORE
    com_scr = COMPUTER_SCORE
    player_scr = PLAYER_SCORE
    if player == "computer":
        computer_logic(com_scr)
    elif player == "player":
        player_logic(player_scr)

def player_logic(previous_scr):
    global PLAYER_SCORE
    print("[Player's turn]\n")
    die_val = roll()
    print("Value in dice: ", die_val)
    if die_val == 1:
        current_scr = 0
        PLAYER_SCORE = current_scr
        print("Oops! looks like a wrong decision!\nYour total score now is: ", current_scr)
        set_current_player_to("computer")
    elif die_val != 1 and die_val <= 6:
        current_scr = previous_scr + die_val
        player_decision = gui()
        if player_decision == 1:    # Roll the dice once more
            previous_scr = current_scr
            player_logic(previous_scr)
        elif player_decision == 2:  # Hold the dice, and keep the score.
            hold(current_scr, "player")

def computer_logic(previous_scr):
    global COMPUTER_SCORE
    print("[Computer's turn]\n")
    die_val = roll()
    print("\nValue in Dice: ", die_val)
    if die_val == 1:
        current_scr = 0
        COMPUTER_SCORE = current_scr
        print("Oh no! I got 1!\nComputer score: ", current_scr)
        set_current_player_to("player")
    elif die_val != 1 and die_val <= 6:
        current_scr = previous_scr + die_val
        decision = comp_dec_hold()
        if decision == 1:
            print("\nI choose to roll the dice.")
            previous_scr = current_scr
            computer_logic(previous_scr)
        elif decision == 2:
            print("\nI choose to hold the dice.")
            hold(current_scr,"computer")

print("\n\n\t\t\tWelcome to the pig game\n")
player_logic(0)









