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
    n_index = 0
    for i, v in enumerate(user_list_input):
        if v == 0:
            n_index = i + 1
            continue
        else:
            break

    user_list_1 = user_list_input [n_index::] +[0 for x in range(n_index)]
    user_list =  [v]

    should_restart = True
    while should_restart:
        should_restart = False
        # value_in_place = 0
        # index_in_place = 0
        # zero_turn = 0
        # index_zero = 0
        # merge = 0
        # count = 0
        for index, value in enumerate(user_list):

            if index == len(user_list)-1:
                    if user_list[index-1] == 0:
                        user_list[index-1] = value + user_list[index-1]
                    else:
                        continue 
            elif value == 0 & user_list[index+1] == 0:
                user_list[index+1] = user_list[index+2]
                user_list[index+2] = 0

        for x in range (2):
            for index, value in enumerate(user_list):
                if index == len(user_list)-1:
                    if user_list[index-1] == 0:
                        user_list[index-1] = value + user_list[index-1]
                    else:
                        continue 
                elif value == user_list[index+1]:
                    user_list[index] = value + user_list[index+1]
                    user_list[index+1] = 0
                    continue
                elif value == 0:
                    user_list[index] = value + user_list[index+1]
                    user_list[index+1] = 0
                    continue
                elif value != user_list[index+1]:
                    continue





            # if 
            #     for i,x in user_list[user_list.index(value)::]:
            #         if value == x:
            #             user_list[index] = value + x
            #             user_list[i] = 0
            #             break
            #         else:
            #             continue 
            # if value == 0:
            #     for i,x in user_list[user_list.index(value)::]:
            #         if x > 0:
            #             user_list[index] = x 
            #             user_list[i] = 0
            #             break
            #         else:
            #             continue 
            #     if user_list[index-1] == x:
            #         user_list[index-1] = value + user_list[index-1]
            #         user_list[index] = 0
            #         continue
                    



                    

            # if value == 0:

            # else:
            #     continue
            # print(x)




            # if index == 0:
            #     if value == user_list[index+1]:
            #         value = value + user_list[index+1]
            #         user_list[index+1] = 0
            #         continue 
            #     else:
            #         continue 
            # elif index == len(user_list) -1:
            #     if value == 0:
            #         continue
            #     elif value != 0:
            #         if value == user_list[index-1]:
            #             value = value + user_list[index-1]
            #             user_list[index] = 0
            #             continue
            # elif index > 0 and value == 0:        
            #     for value in user_list:
            #         if value == 0:
            #             zero_index = user_list.index(value)
            #             break
            #         else:
            #             continue
            #     value = user_list[index+1]
            #     user_list[index] = value
            #     user_list[index+1] = 0
            #     if value  == user_list[index-1]:
            #         user_list[index-1] = value + user_list[index-1]
            #         user_list[index] = 0
            #     if user_list[index-1] == 0:
            #         user_list[index-1] = value
            #         user_list[index] = 0
            # elif index > 0 and value != 0:
            #     if value == user_list[index-1]:
            #         value = value + user_list[index-1]
            #         user_list[index-1] = 0
            #         value = user_list[index+1]
            #         user_list[index+1] = 0

            #     else:
            #         continue
                

            # # if index == 0 and value > 0:
            #     value_in_place = value
            #     index_in_place = index
            # if index > 0 and zero_turn > 0 and value_in_place == 0:
            #     value_in_place = value
            #     index_in_place = index
            #     index_zero = index
            # if value == 0:
            #     if zero_turn == 0:
            #         index = user_list.index(0) 
            #         index_zero = index
            #         zero_turn += 1

            # if index  > 0 and value > 0 and value == value_in_place:
            #     user_list[index_in_place] = value_in_place + value
            #     value_in_place = 0
            #     user_list[index] = 0
            #     index_in_place = index
            #     index_zero = index
            # if index  > 0 and value >= 0 and value != value_in_place and merge > 0:
            #     if zero_turn > 0 :
            #         user_list[index_zero] = value
            #         user_list[index] = 0
            #         value_in_place = value
            #         index_in_place = index_zero
            #         #if user_list[index-2] == value and merge == 0:
                        # user_list[index-2] = value + user_list[index-2]
                        # value_in_place = 0
                        # user_list[index-1] = 0
                        # index_in_place = index
                        # index_zero = index-1
                        # merge = 1
                        # continue
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
