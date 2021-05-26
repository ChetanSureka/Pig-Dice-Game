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
        print("Your total score is: ", total_scr)
        if total_scr >= 100:
            print("YOU WIN !!!\n\nGame Over")
        else:
            PLAYER_SCORE = total_scr
            print("The die is passed on to the computer.")
            
    else:
        print("The die is passed on to the next player.")
    return total_scr

def gui():
    print("Select any one option:\n1. Roll\n2. Hold")
    player_decision = int(input("Enter your choice: "))
    return player_decision

def comp_dec_hold():
    decision = random.randint(1,2)
    return decision

def player_logic(previous_scr):
    die_val = roll()
    print("Value in dice: ", die_val)
    if die_val == 1:
        current_scr = 0
    elif die_val != 1 and die_val <= 6:
        current_scr = previous_scr + die_val
        player_decision = gui()
        if player_decision == 1:
            previous_scr = current_scr
            player_logic(previous_scr)
        elif player_decision == 2:
            hold(current_scr, "player")

def computer_logic(previous_scr):
    die_val = roll()
    print("Value in Dice: ", die_val)
    if die_val == 1:
        current_scr = 0
    elif die_val != 1 and die_val <= 6:
        current_scr = previous_scr + die_val
        decision = comp_dec_hold()
        if decision == 1:
            print("I choose to roll the dice.")
            previous_scr = current_scr
            computer_logic(previous_scr)
        elif decision == 2:
            print("I choose to hold the dice.")
            hold(current_scr)

player_logic(0)









