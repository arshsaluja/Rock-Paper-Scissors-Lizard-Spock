"""
Implementing RPSLS for Practice Project
"""

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
    
print(name_to_number("rock"))		# output - 0
print(name_to_number("Spock"))		# output - 1
print(name_to_number("paper"))		# output - 2
print(name_to_number("lizard"))		# output - 3
print(name_to_number("scissors"))	# output - 4
print(number_to_name(0))
print(number_to_name(1))
print(number_to_name(2))
print(number_to_name(3))
print(number_to_name(4))
