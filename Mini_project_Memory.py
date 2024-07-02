# implementation of card game - Memory

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

a_list = random.sample(range(0, 8), 8)
b_list = random.sample(range(0, 8), 8)
c_list = a_list + b_list
exposed = len(c_list) * [False]


# helper function to initialize globals
def new_game():
    random.shuffle(c_list)
    return c_list
  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed
    ball_pos = list(pos)
    ff = 50
    gg = 0
    for index, item in enumerate(exposed):
        if gg <= ball_pos[0] <= ff and item == False:
            exposed[index] = True
            break
        else:
            ff += 50
            gg += 50
            continue
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global c_list
    global exposed
    width = 10
    for x in c_list:
        canvas.draw_text(str(x), (width, 65), 50, 'Red')
        width += 50
    f = 50
    g = 0
    c = 0

    for x in exposed:
        if x is False:
            color = 'green'
        else:
            color = None
        canvas.draw_polygon([(g, 0),(f, 0), (f, 100), (g, 100)], 2, 'Red', color)
        f += 50
        g += 50


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric