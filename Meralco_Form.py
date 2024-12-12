import tkinter as tk
from idlelib.run import MyHandler
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

#window
window = tk.Tk()
window.title("Meralco Form")
window.geometry('700x900')

class design_gui_interface():

    def heading_design(self, x, y, text_value):
        self.text_value = text_value
        self.heading = Label(text=text_value, fg='black', font=('Algerian', 15, 'bold'))
        self.heading.place(x=x, y=y)

    def frames(self,x ,y):
        self.frame1 =  Frame(window, width=100, height=50, border=0, bg='orange')
        self.frame1.place(x=x, y=y)

    def textbox_design(self, x, y):
        self.textbox = Text(width=78, height=1, fg='black', bg='white', font=('Arial', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=38, height=1, fg='black', bg='white', font=('Arial', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def textbox_design3(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='white', font=('Arial', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, fg='black', font=('Calibre', 10))
        self.lbl.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(window, image=self.bck_pic)
        self.lbl.place(x=x, y=y)

#instantiation of the class
my_gui_design = design_gui_interface()

#call for heading
my_gui_design.heading_design(x=225, y=50, text_value='APPLICANT INFORMATION')
my_gui_design.heading_design(x=190, y=495, text_value='REPRESENTATIVE INFORMATION')
my_gui_design.heading_design(x=190, y=685, text_value='DOCUMENTARY REQUIREMENTS')

# Label for applicant information
my_gui_design.label_design(x=40, y=80, text_value='Applicant Number')
my_gui_design.label_design(x=40, y=120, text_value='Service ID Number')
my_gui_design.label_design(x=40, y=160, text_value='Surname')
my_gui_design.label_design(x=40, y=200, text_value='First Name')
my_gui_design.label_design(x=40, y=240, text_value='Middle Name')
my_gui_design.label_design(x=40, y=280, text_value='Birth Date')
my_gui_design.label_design(x=360, y=280, text_value='Gender')
my_gui_design.label_design(x=40, y=320, text_value='Civil Status')
my_gui_design.label_design(x=360, y=320, text_value='Nationality')
my_gui_design.label_design(x=40, y=360, text_value='Cellphone Number')
my_gui_design.label_design(x=360, y=360, text_value='Landline Number')
my_gui_design.label_design(x=40, y=400, text_value='Email Address')
my_gui_design.label_design(x=40, y=440, text_value='Complete Service Address')

# Textbox for applicant information
my_gui_design.textbox_design(x=40, y=100)
my_gui_design.textbox_design(x=40, y=140)
my_gui_design.textbox_design(x=40, y=180)
my_gui_design.textbox_design(x=40, y=220)
my_gui_design.textbox_design(x=40, y=260)
my_gui_design.textbox_design2(x=360, y=300)
my_gui_design.textbox_design2(x=40, y=300)
my_gui_design.textbox_design2(x=360, y=340)
my_gui_design.textbox_design2(x=40, y=340)
my_gui_design.textbox_design2(x=360, y=380)
my_gui_design.textbox_design2(x=40, y=380)
my_gui_design.textbox_design(x=40, y=420)
my_gui_design.textbox_design(x=40, y=460)

# Label for representative information
my_gui_design.label_design(x=40, y=530, text_value='Surname')
my_gui_design.label_design(x=250, y=530, text_value='First Name')
my_gui_design.label_design(x=460, y=530, text_value='Middle Name')
my_gui_design.label_design(x=40, y=580, text_value='Contact Address')
my_gui_design.label_design(x=40, y=630, text_value='Cellphone Number')
my_gui_design.label_design(x=360, y=630, text_value='Landline Number')

#textbox for representative information
my_gui_design.textbox_design3(x=40, y=550)
my_gui_design.textbox_design3(x=250, y=550)
my_gui_design.textbox_design3(x=460, y=550)
my_gui_design.textbox_design(x=40, y=600)
my_gui_design.textbox_design2(x=40, y=650)
my_gui_design.textbox_design2(x=360, y=650)

# label for documentary requirements
my_gui_design.label_design(x=40, y=720, text_value='*Photocopy of any recent Meralco Bill')
my_gui_design.label_design(x=40, y=740, text_value='*Photocopy of any ONE valid Identification Card of Registered Customer (front & back)')
my_gui_design.label_design(x=40, y=760, text_value='*For Representative Letter of Authorization from the Registered Customer ')

# Adding combo for gender
n = tk.StringVar()
combo_field1 = ttk.Combobox(window, width=48, textvariable=n)
combo_field1['values'] = (' Male', 'Female')
combo_field1.place(x=360, y=300)
combo_field1.current()

# Adding combo for civil status
n = tk.StringVar()
combo_field1 = ttk.Combobox(window, width =48, textvariable = n)
combo_field1['values'] = (' Single', ' Married ', ' Widow', ' Legally Separated', ' Annulled')
combo_field1.place(x=40, y=340)
combo_field1.current()

# call image to display
upload_image = my_gui_design.image_design(image_location= r"C:\Users\Jester\Documents\GitHub\PLDL_CPE201\MERALCOO.jpg", x=20, y=10, length=70, width=70)

window.mainloop()