from tkinter import *
import re

class ReDemo:

    def __init__(self,master):
        self.master = master

        self.promptdisplay = label(self.master, anchor =W,
                text='Enter a [erl-style regular expression:')
        self.promptdisplay.pack(side=TOP, fill=X)

        self.regexdisplay = Entry(self.master)
        self.regexdisplay.pack(fill=X)
        self.regexdisplay.focus_set()

        self.addoptions()

        self.statusdisplay = Label(self.master, text="", anchor=W)
        self.statusdisplay.pack(side=TOP, fill=X)

        self.labeldisplay = Label(self.master, anchor=W)
        self.statusdisplay.pack(side=TOP, fill=X)
        





def main():
    root = tk()
    demo = ReDemo(root)
    root.protocol('WM_DELETED_WINDOW', root.quit)
    root.mainloop()

if __name__ =='__main__':
    main()
