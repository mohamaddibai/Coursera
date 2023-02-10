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

#
    should_restart = True
    while should_restart:
        should_restart = False
        value_in_place = 0
        index_in_place = 0
        index_zero = 0
        merge = 0
        for index, value in enumerate(user_list):
            if index == 0:
                value_in_place = value
                index_in_place = index
                continue
            elif value == 0:
                value_in_place = value
                index_in_place = index
                index_zero = index
                continue
            elif index  > 0 and value > 0 and value == value_in_place:
                user_list[index_in_place] = value_in_place + value
                value_in_place = 0
                user_list[index] = 0
                index_in_place = index
                index_zero = index
                continue
            elif index  > 0 and value >= 0 and value != value_in_place:
                if index_zero > 0 :
                    user_list[index_zero] = value
                    user_list[index] = 0
                    index_zero = index
                    if user_list[index-2] == value and merge == 0:
                        user_list[index-2] = value + user_list[index-2]
                        value_in_place = 0
                        user_list[index-1] = 0
                        index_in_place = index
                        index_zero = index-1
                        merge = 1
                        continue
                continue 
        print(user_list)

        # iterator = iter(user_list)
        # first = next(iterator)
        # if not all(first == x for x in iterator):
        #     should_restart = 
            

         
    #     loop_continue =  input("Press Enter to continue...")
    #     if loop_continue == "":
    #         should_restart = True
    #         else:
    #             print(user_list)  
    #             break  
            # if index_in_place > 0 and value == 0 :
                # it take the index of this value index_zero
                # value_in_place =0 
                #continue
merge()
