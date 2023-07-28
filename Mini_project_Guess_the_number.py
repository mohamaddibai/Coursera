# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import math

# Initialize global variables
secret_number = 0
num_range = 7
n = 0
message = "Guess the number"

# Helper function to start and restart the game
def new_game():
    global secret_number
    secret_number = random.randint(0, num_range)
    #print('secret_number=%d range', secret_number)


# Define event handlers for control panel
def range100():
    global num_range
    num_range = 7
    n = 0
    new_game()


def range1000():
    global num_range
    num_range = 10
    n = 0
    new_game()
 
def input_guess(player_guess):
    # main game logic goes here	
    global message
    global n
    n +=1
    player_guess = int(player_guess)
    if player_guess == secret_number:
        message = "Correct! You win!"
        n = 0
        new_game()
    elif player_guess < secret_number:
        message = "Higher! "
        message += 'remaining guesses: ' + str(num_range - n)
    elif player_guess > secret_number:
        message = "Lower! "
        message += 'remaining guesses: ' + str(num_range - n)
    elif n == num_range:
        message = 'You used all your chances! '
    
    

    
# create frame

f = simplegui.create_frame('Guess the number', 200, 200)
# register event handlers for control elements and start frame
f.add_button('Range is [0, 100)', range100, 200)
f.add_button('Range is [0, 1000)', range1000, 200)
f.add_input('Enter a guess', input_guess, 200)
# call new_game 
def draw(canvas):
    canvas.draw_text(message, [50,112], 10, "Red")
f.set_draw_handler(draw)
new_game()
f.start()
# always remember to check your completed program against the grading rubric
