# template for "Stopwatch: The Game"
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# define global variables
number_time = 0
success_time = 0
num_stop = 0
stop_count = False


def timer_handler():
    global number_time
    number_time += 1 
    # return number_time

timer = simplegui.create_timer(100, timer_handler)
timer.start()



# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(sec):
    seconds = sec % 600
    seconds_2 = seconds // 10
    tenth_sec = seconds % 10
    minutes = sec // 600
    x = "%d:%02d.%d" % (minutes, seconds_2, tenth_sec)
    return x, tenth_sec

stop_value = format(number_time)[1]
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def ResetButton():
    global number_time
    number_time = 0
    # return number_time

def StopButton():
    global stop_count
    stop_count = True
    timer.stop()


def score():
    global stop_count
    global stop_value
    global success_time
    global num_stop

    if stop_count is True:
        num_stop +=1
        if stop_value == 0:
            success_time += 1
        else:
            pass
    stop_count = False
    return num_stop, success_time


def startButton():
    timer.start()

# define event handler for timer with 0.1 sec interval


# define draw handlerx
def draw(canvas):
    canvas.draw_text(format(number_time)[0],[100, 112], 20, "Red")
    canvas.draw_text(str(score()),[300, 20], 20, "Red")
    
# create frame
frame = simplegui.create_frame('Testing', 400, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button('Start', startButton)
frame.add_button('Stop', StopButton)
frame.add_button('Reset', ResetButton)

# start frame
frame.start()

# Please remember to review the grading rubric
