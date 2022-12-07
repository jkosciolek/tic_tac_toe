import tkinter.messagebox
from tkinter import *
from PIL import ImageTk,Image


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Tic Tac Toe")
        self.iconphoto(False, PhotoImage(file='logo-cutout.png'))
        # root.iconbitmap('logo-cutout.ico')
        self.configure(bg='#303030')


        # placing root in a middle of the user's screen
        global app_width, app_height, x, y
        app_width = 900
        app_height = 600

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.resizable(False, False)

        # labels
        self.myLabel = Label(self, text="Tic Tac Toe", font=("Chalkboard", 100), bg='#303030', fg='#7F1E90')

        # buttons
        self.myButton = Button(self, text="Singleplayer", font=("Chalkboard", 23), command=self.button_single, height=3, width=30)
        self.myButton2 = Button(self, text="Multiplayer", font=("Chalkboard", 23), command=self.button_multi, height=3, width=30)
        self.myButton3 = Button(self, text="Quit", font=("Chalkboard", 23), command=self.destroy, height=2, width=30)

        # packing
        # self.myLabel.grid(row=0, column=2, columnspan=3, padx=10, pady=10)
        # self.myButton.grid(row=1, column=3, columnspan=1, padx=10, pady=10)
        # self.myButton2.grid(row=2, column=3, columnspan=1, padx=10, pady=10)
        # self.myButton3.grid(row=3, column=0, columnspan=1, padx=10, pady=10)

        self.myLabel.pack(pady=60)
        self.myButton.pack(pady=10)
        self.myButton2.pack(pady=10)
        self.myButton3.pack(pady=10)

    def button_single(self):
        top = Toplevel()
        top.title("Tic Tac Toe")
        top.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        top.resizable(False, False)

    def button_multi(self):
        top = Toplevel()
        top.title("Tic Tac Toe")
        top.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        top.resizable(False, False)



