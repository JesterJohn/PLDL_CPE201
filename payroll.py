from tkinter import *
from PIL import Image, ImageTk

class design_gui_interface():

    def __init__(self, window):
        self.window = window

    def heading_design1(self, x, y, text_value):
        self.text_value = text_value
        self.heading = Label(text=text_value, fg='black', font=('Times New Roman', 25, 'bold'))
        self.heading.place(x=x, y=y)

    def textbox_design(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='white', font=('Arial', 12))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='light gray', font=('Arial', 12))
        self.textbox.place(x=x, y=y)

    def label_design1(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, font=('Arial', 8,))
        self.lbl.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, font=('Arial', 10, 'bold'))
        self.lbl.place(x=x, y=y)

    def button_design1(self, x, y):
        self.upload_button = Button(width=10,padx=10,text='SEARCH',bg='red', fg='white',cursor='hand2',border=5)
        self.upload_button.place(x=x, y=y)

    def button_design2(self, x, y):
        self.upload_button = Button(width=9, padx=10, text='GROSS INCOME', bg='blue', fg='white', cursor='hand2', border=5)
        self.upload_button.place(x=x, y=y)

    def button_design3(self, x, y):
        self.upload_button = Button(width=8, padx=10, text='NET INCOME', bg='blue', fg='white', cursor='hand2', border=5)
        self.upload_button.place(x=x, y=y)

    def button_design4(self, x, y):
        self.upload_button = Button(width=6, padx=10, text='SAVE', bg='cyan', fg='black', cursor='hand2', border=5)
        self.upload_button.place(x=x, y=y)

    def button_design5(self, x, y):
        self.upload_button = Button(width=6, padx=10, text='UPDATE', bg='cyan', fg='black', cursor='hand2', border=5)
        self.upload_button.place(x=x, y=y)

    def button_design6(self, x, y):
        self.upload_button = Button(width=5, padx=10, text='NEW', bg='yellow', fg='black', cursor='hand2', border=5)
        self.upload_button.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(self.window, image=self.bck_pic)
        self.lbl.place(x=x, y=y)


