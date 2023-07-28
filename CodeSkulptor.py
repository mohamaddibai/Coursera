# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor is tested to run in recent versions of
# Chrome, Firefox, Safari, and Edge.

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"

def range100():
    # button that changes the range to [0,100) and starts a new game 
    global message
    random_number = random.randint(0, 100)
    message = str(random_number)

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global message
    random_number = random.randint(0, 100)
    message = str(random_number)

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.add_button('Range is [0, 100)', range100, 200)
frame.add_button('Range is [0, 1000)', range1000, 200)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
