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
    user_list = list(map(int, input_string.split()))

    for num, name in enumerate(user_list):
    #list is here
        user_list = list(map(int, input_string.split()))
    #loop starts (takes the value from the list)
    should_restart = True
    while should_restart:
        should_restart = False
        for index, value in enumerate(user_list):
            value_in_place = 0
            index_in_place = 0
            index_zero = 0 
            if index == 0:
                value_in_place = value
                continue
            if index_in_place > 0 and value > 0 and value == value_in_place:
                user_list[index_in_place] = value_in_place + value
                value_in_place = 0
                index_in_place = value
                continue
            if index_zero > 0 :
                user_list[index_zero] = value
                index_zero = user_list.index(value)
                user_list[index] = 0
                index_zero = 0
                continue
            if index == 0:
                # set the current value to the value_in_place variable.
                value_in_place = value
                continue
            if index == len(user_list) - 1:
                    print(user_list)
                    loop_continue =  input("Press Enter to continue...")
                    if loop_continue == "":
                        should_restart = True
                    else:
                        print(user_list)  
                        break  
            # if index_in_place > 0 and value == 0 :
                # it take the index of this value index_zero
                # value_in_place =0 
                #continue

