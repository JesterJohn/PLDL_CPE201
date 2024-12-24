from tkinter import *
from PIL import Image, ImageTk

class design_gui_interface:

    def __init__(self, window):
        self.window = window

    def heading_design(self, x, y, text_value):
        heading = Label(self.window, text=text_value, fg='black',bg='white', font=('Arial', 20, 'bold'))
        heading.place(x=x, y=y)

    def frames(self, x, y):
        frame = Frame(self.window, width=450, height=500, border=0, bg='white')
        frame.place(x=x, y=y)

    def textbox_design(self, x, y):
        textbox = Entry(self.window, width=48, fg='black', bg='light gray', font=('Arial', 10))
        textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        lbl = Label(self.window, text=text_value, bg='white', font=('Calibre', 10))
        lbl.place(x=x, y=y)

    def button_design1(self, x, y):
        upload_button = Button(self.window, width=10, padx=10, text='Facebook', bg='blue', fg='white', cursor='hand2',border=5)
        upload_button.place(x=x, y=y)

    def button_design2(self, x, y):
        upload_button = Button(self.window, width=10, padx=10, text='Google', bg='white', fg='black', cursor='hand2', border=5)
        upload_button.place(x=x, y=y)

    def button_design3(self, x, y):
        upload_button = Button(self.window, width=10, padx=10, text='Apple', bg='black', fg='white', cursor='hand2', border=5)
        upload_button.place(x=x, y=y)

    def button_design4(self, x, y):
        upload_button = Button(self.window, width=10, padx=10, text='Log in', bg='red', fg='white', cursor='hand2', border=5)
        upload_button.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        image = Image.open(image_location)
        bck_pic = ImageTk.PhotoImage(image.resize((length, width)))
        lbl = Label(self.window, image=bck_pic)
        lbl.image = bck_pic
        lbl.place(x=x, y=y)

