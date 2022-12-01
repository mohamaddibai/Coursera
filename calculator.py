"""
it finds the Square root of a number

"""
import math
import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color

layout = [  [sg.Text('Calculator')],
            [sg.Text('find the Square Root :'), sg.InputText()],
            [sg.Button('Calculate the Square Root'), sg.Button('Calculate the Sin'), sg.Button('Cancel')] ]
# Create the Window
window = sg.Window('Window Calculator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Calculate the Square Root':
        x1 = values[0]
        try:
            answer = int(x1)
            try:
                print(f'Square Root of {answer} is {math.sqrt(answer)}')
            except ValueError:
                print(f'You entered {answer}, which is not a positive number.')
        except ValueError as ve:
            print('You are supposed to enter a number')
    if  event == 'Calculate the Sin':
        x2 = values[0]
        try:
            answer = int(x2)
            try:
                print(f'The Sin of {answer} is {math.sin(answer)}')
            except ValueError:
                print(f'You entered {answer}, which is not a positive number.')
        except ValueError as ve:
            print('You are supposed to enter a number')

window.close()
