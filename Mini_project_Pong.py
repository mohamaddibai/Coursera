# Implementation of classic arcade game Pong
import random
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos= [WIDTH/2,HEIGHT/2]
ball_vel = [random.uniform(-0.5, 0.5) ,random.uniform(-0.5, 0.5)]
paddle1_pos = [[0,150], [0,250]]
paddle2_pos = [[600,150], [600,250]]
paddle1_vel = [10,10]
paddle2_vel = [10,10]
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction=None):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos= [WIDTH/2,HEIGHT/2]
    global score1, score2
    if direction is None:
        x= [[random.randrange(1, 3),random.randrange(2, 4)],[-random.randrange(1, 3),random.randrange(2, 4)]]
        ball_vel= random.choice(x)
        pass
    elif direction == RIGHT:
        ball_vel= [random.randrange(1, 3),random.randrange(2, 4)]
        score2 += 1
    elif direction == LEFT:
        ball_vel = [-random.randrange(1, 3),random.randrange(2, 4)]
        score1 += 1
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,ball_pos  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball()

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_pos
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(str(score1),[150, 40], 30, "white")  
    canvas.draw_text(str(score2),[450, 40], 30, "white") 
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]   
    if ball_pos[1] > HEIGHT-BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "black")
    # update paddle's vertical position, keep paddle on the screen
    # paddle1_pos[0][1] += paddle1_vel[0]
    # paddle2_pos[0][1] += paddle2_vel[1]
    # paddle1_pos[1][1] += paddle1_vel[0]
    # paddle2_pos[1][1] += paddle2_vel[1] 
    # draw paddles
    canvas.draw_line(paddle1_pos[0], paddle1_pos[1], 10, 'white')
    canvas.draw_line(paddle2_pos[0], paddle2_pos[1], 10, 'white') 
    # determine whether paddle and ball collide    
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        if paddle1_pos[0][1] <= ball_pos[1] <= paddle1_pos[1][1]:
            ball_vel[0] = - ball_vel[0] * (1+0.10)
        else:
            spawn_ball(RIGHT)  
    if ball_pos[0] > WIDTH-PAD_WIDTH-BALL_RADIUS:
        if paddle2_pos[0][1] <= ball_pos[1] <= paddle2_pos[1][1]:
            ball_vel[0] = - ball_vel[0] * (1+0.10)
        else:
            spawn_ball(LEFT)

    # draw scores   
def keydown(key):
    global paddle1_vel, paddle2_vel,paddle1_pos,paddle2_pos
    if chr(key) == 'S' and paddle1_pos[1][1] < HEIGHT:
        paddle1_pos[0][1] += paddle1_vel[1]
        paddle1_pos[1][1] += paddle1_vel[1]
    if chr(key) == '(' and paddle2_pos[1][1] < HEIGHT :
        paddle2_pos[0][1] += paddle2_vel[1]
        paddle2_pos[1][1] += paddle2_vel[1]

def keyup(key):
    global paddle1_vel, paddle2_vel,paddle1_pos,paddle2_pos
    if chr(key) == 'W' and  paddle1_pos[0][1] > 0:
        paddle1_pos[0][1] -= paddle1_vel[1]
        paddle1_pos[1][1]-= paddle1_vel[1]
    if chr(key) == '&' and  paddle2_pos[0][1] > 0:
        paddle2_pos[0][1] -= paddle2_vel[1]
        paddle2_pos[1][1] -= paddle2_vel[1]
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', new_game) 
# start frame
new_game()
frame.start()