# my_list = []

# def my_function(number):
#     global my_list
#     my_list.append(number)
#     if number == 1:
#         print(my_list)
#         return 
#     elif number % 2 == 0:
#         new_number = number / 2
#         number = new_number
#     elif number % 2 == 1:
#         new_number = (number * 3) + 1
#         number = new_number
#     my_function(number)


#  # Print the list after processing each number

# my_function(217)
# print(max(my_list))

import this 
from tkinter import * 
from tkinter import messagebox  
rot13 = str.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm" 
)  
def main_window(root: Tk): 
    frame = Frame(root) 
    frame.pack()  
    zen_button = Button(frame, text="Python Zen", command=show_zen) 
    zen_button.pack(side=LEFT)  
def show_zen(): 
    messagebox.showinfo("Zen of Python", this.s.translate(rot13))  
if __name__ == "__main__": 
    root = Tk() 
    main_window(root) 
    root.mainloop() 