"""
Merge function for 2048 game.
"""

def merge():
    """
    Function that merges a single row or column in 2048.
    """
    # capture the input
    input_string = input('Enter list of your numbers with a space between each  ')
    print("\n")
    user_list_input = list(map(int, input_string.split()))
    zero_list = [0] * len(user_list_input)
    saved = 0

    should_restart = True
    while should_restart:
        should_restart = False
        for index, value in enumerate(user_list_input):
            if value > 0:
                if value == saved :
                    zero_list[zero_list.index(saved)] = value + saved 
                    saved = 0
                    continue
                if value != saved:
                    zero_list[zero_list.index(0)] = value
                    saved = value
                    continue
        print(zero_list)
merge()
