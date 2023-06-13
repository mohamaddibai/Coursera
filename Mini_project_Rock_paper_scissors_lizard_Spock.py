# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random 
# helper functions

def name_to_number(name):
    '''
    return the number corresponding to the string name
    
    '''
    if name == 'rock':
        return 0
    elif name == 'spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return 'invalid name'


def number_to_name(number):
    '''
    return the string corresponding to the number

    '''
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'invalid number'
    

def rpsls(player_choice): 
    '''
    compute the result of the Rock-Paper-Scissors-Lizard-Spock game

    '''
    # print a blank line to separate consecutive games
    print('')
    # print the player's choice
    print('You chose:', player_choice)
    # print the computer's choice
    computer_choice = random.randrange(0, 4)
    print('The computer chose:', number_to_name(computer_choice))
    # print a blank line to separate consecutive games
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # print a blank line to separate consecutive games
    # if the player's choice is equal to the computer's choice
    if player_number == computer_choice:
        # print out the message for a draw
        print('It is a draw!')
    # if the player's choice is not equal to the computer's choice
    elif player_number > computer_choice:
        # print out the message for a win
        print('You win!') 
    # if the player's choice is not equal to the computer's choice
    elif player_number < computer_choice:
        # print out the message for a loss
        print('You lose!')

    # compute difference of comp_number and player_number modulo five


    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


