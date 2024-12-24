from tkinter import *
from PIL import Image, ImageTk

class design_gui_interface():

    def __init__(self, window):
        self.window = window

    def heading_design1(self, x, y, text_value):
        self.text_value = text_value
        self.heading = Label(text=text_value, fg='black', font=('Times New Roman', 18, 'bold'))
        self.heading.place(x=x, y=y)

    def heading_design2(self, x, y, text_value):
        self.text_value = text_value
        self.heading = Label(text=text_value, fg='black', font=('Times New Roman', 12, 'bold'))
        self.heading.place(x=x, y=y)

    def frames1(self, x, y):
        frame = Frame(self.window, width=800, height=130, border=0, bg='light gray')
        frame.place(x=x, y=y)

    def frames2(self, x, y):
        frame = Frame(self.window, width=800, height=110, border=0, bg='light gray')
        frame.place(x=x, y=y)

    def frames3(self, x, y):
        frame = Frame(self.window, width=800, height=220, border=0, bg='light gray')
        frame.place(x=x, y=y)

    def label_design1(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg='light gray', font=('Arial', 10))
        self.lbl.place(x=x,  y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(width=20, height=1, fg='black', bg='white', font=('Arial', 8))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='white', font=('Arial', 8))
        self.textbox.place(x=x, y=y)

    def textbox_design3(self, x, y):
        self.textbox = Text(width=30, height=1, fg='black', bg='white', font=('Arial', 8))
        self.textbox.place(x=x, y=y)

    def textbox_design4(self, x, y):
        self.textbox = Text(width=35, height=1, fg='black', bg='white', font=('Arial', 8))
        self.textbox.place(x=x, y=y)

    def textbox_design5(self, x, y):
        self.textbox = Text(width=50, height=1, fg='black', bg='white', font=('Arial', 8))
        self.textbox.place(x=x, y=y)

    def textbox_design6(self, x, y):
        self.textbox = Text(width=37, height=1, fg='black', bg='white', font=('Arial', 8))
        self.textbox.place(x=x, y=y)

    def textbox_design7(self, x, y):
        self.textbox = Text(width=60, height=1, fg='black', bg='white', font=('Arial', 8))
        self.textbox.place(x=x, y=y)

    def textbox_design8(self, x, y):
        self.textbox = Text(width=73, height=1, fg='black', bg='white', font=('Arial', 8))
        self.textbox.place(x=x, y=y)

    def textbox_design9(self, x, y):
        self.textbox = Text(width=126, height=1, fg='black', bg='white', font=('Arial', 8))
        self.textbox.place(x=x, y=y)

    def textbox_design10(self, x, y):
        self.textbox = Text(width=62, height=1, fg='black', bg='white', font=('Arial', 8))
        self.textbox.place(x=x, y=y)

    def button_design1(self, x, y):
        self.upload_button = Button(width=10, padx=10, text='Choose File', bg='white', fg='black', cursor='hand2', border=5)
        self.upload_button.place(x=x, y=y)

    def button_design2(self, x, y):
        self.upload_button = Button(width=10, padx=10, text='Save', bg='blue', fg='white', cursor='hand2', border=5)
        self.upload_button.place(x=x, y=y)

    def button_design3(self, x, y):
        self.upload_button = Button(width=10, padx=10, text='Cancel', bg='white', fg='black', cursor='hand2', border=5)
        self.upload_button.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(self.window, image=self.bck_pic)
        self.lbl.place(x=x, y=y)
