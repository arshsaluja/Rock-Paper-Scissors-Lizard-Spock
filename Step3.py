"""
Implementing RPSLS for Practice Project
"""
import random
def name_to_number(name):
    """
    Take string name as input (rock-Spock-paper-lizard-scissors)
    and returns integer (0-1-2-3-4)
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
def number_to_name(number):
    if number==0:
        return"rock"
    elif number==1:
        return"Spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    else:
        return "scissors"
def rpsls(player_choice):
    # print a blank line to separate consecutive games
    print("\n")
    # print out the message for the player's choice
    # convert the player's choice to 
    #player_number using the function name_to_number()
    player_number=name_to_number(player_choice)
    print("Player chooses "+number_to_name(player_number))
    # compute random guess for comp_number using random.randrange()
    comp_number =random.randrange(5)#because it returns random nos -0,1,2,3,34
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice=number_to_name(comp_number)
    # print out message for computer's choice
    print("Computer chooses "+comp_choice)
    # compute difference of player_number and comp_number modulo five
    c=(player_number-comp_number)%5
    # use if/elif/else to determine winner and print winner message
    
print(rpsls("rock"))		# output - 0
print(rpsls("Spock"))		# output - 1
print(rpsls("paper"))		# output - 2
print(rpsls("lizard"))		# output - 3
print(rpsls("scissors"))	# output - 4
