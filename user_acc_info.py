from tkinter import *
from PIL import Image, ImageTk

class design_gui_interface:

    def __init__(self, window):
        self.window = window

    def heading_design(self, x, y, text_value):
        heading = Label(self.window, text=text_value, fg='black', font=('Arial', 20, 'bold'))
        heading.place(x=x, y=y)

    def frames(self, x, y):
        frame1 = Frame(self.window, width=820, height=300, border=0, bg='#e4e9eb')
        frame1.place(x=x, y=y)

    def textbox_design(self, x, y):
        textbox = Text(self.window, width=30, height=2, fg='black', bg='white', font=('Arial', 8, 'bold'))
        textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        textbox = Text(self.window, width=18, height=2, fg='black', bg='light gray', font=('Arial', 8, 'bold'))
        textbox.place(x=x, y=y)

    def textbox_design3(self, x, y):
        textbox = Text(self.window, width=22, height=2, fg='black', bg='light gray', font=('Arial', 8, 'bold'))
        textbox.place(x=x, y=y)

    def textbox_design4(self, x, y):
        textbox = Text(self.window, width=45, height=2, fg='black', bg='light gray', font=('Arial', 8, 'bold'))
        textbox.place(x=x, y=y)

    def textbox_design5(self, x, y):
        textbox = Text(self.window, width=45, height=2, fg='black', bg='white', font=('Arial', 8, 'bold'))
        textbox.place(x=x, y=y)

    def textbox_design6(self, x, y):
        textbox = Text(self.window, width=22, height=2, fg='black', bg='white', font=('Arial', 8, 'bold'))
        textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        lbl = Label(self.window, text=text_value, bg='#e4e9eb', font=('Calibre', 10))
        lbl.place(x=x, y=y)

    def button_design1(self, x, y):
        upload_button = Button(self.window, width=10, padx=10, text='Update', bg='blue', fg='white', cursor='hand2', border=5)
        upload_button.place(x=x, y=y)

    def button_design2(self, x, y):
        upload_button = Button(self.window, width=10, padx=10, text='Delete', bg='yellow', fg='black', cursor='hand2', border=5)
        upload_button.place(x=x, y=y)

    def button_design3(self, x, y):
        upload_button = Button(self.window, width=10, padx=10, text='Cancel', bg='white', fg='black', cursor='hand2', border=5)
        upload_button.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        image = Image.open(image_location)
        bck_pic = ImageTk.PhotoImage(image.resize((length, width)))
        lbl = Label(self.window, image=bck_pic)
        lbl.image = bck_pic
        lbl.place(x=x, y=y)
