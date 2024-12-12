import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

#window
window = tk.Tk()
window.title("Student Assesment Form")
window.geometry('1520x900')

class design_gui_interface():

    def heading_design(self, x, y, text_value):
        self.text_value = text_value
        self.heading = Label(text=text_value, fg='maroon', font=('Algerian', 30, 'bold'))
        self.heading.place(x=x, y=y)

    def frames(self, x, y):
        self.frame1 = Frame(window, width=1100, height=200, border=0,bg='maroon')
        self.frame1.place(x=x, y=y)

    def frames2(self, x, y):
        self.frame2 = Frame(window, width=1100, height=40, border=5, bg='light gray')
        self.frame2.place(x=x, y=y)

    def textbox_design(self, x, y):
        self.textbox = Text(width=30, height=1, fg='black', bg='white', font=('Arial', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, fg='white', bg='maroon', font=('Calibre', 14))
        self.lbl.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, fg='black', bg='light gray', font=('Calibre', 16))
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

#call image to display
uploaded_image = my_gui_design.image_design(r"C:\Users\Jester\Documents\GitHub\PLDL_CPE201\LPUC.jpg",0, 0, 1517, 870)

#call for frame 1
my_gui_design.heading_design(x=200, y=60, text_value='LYCEUM OF THE PHILIPPINES OF THE UNIVERSITY - CAVITE')
my_gui_design.frames(x=50, y=195)
my_gui_design.frames(x=350, y=470)
#call for frame 2
my_gui_design.frames2(x=50, y=160)
my_gui_design.frames2(x=350, y=435)

#Label for Student Information
my_gui_design.label_design(x=70, y=220, text_value='Student Name:')
my_gui_design.label_design(x=70, y=300, text_value='Student Number:')
my_gui_design.label_design(x=450, y=220, text_value='Date of Birth')
my_gui_design.label_design(x=450, y=300, text_value='Gender:')
my_gui_design.label_design(x=800, y=220, text_value='Contact Information:')
my_gui_design.label_design(x=800, y=300, text_value='Emergency Contact:')

#Textbox for Student Information
my_gui_design.textbox_design(x=70, y=260)
my_gui_design.textbox_design(x=70, y=340)
my_gui_design.textbox_design(x=450, y=260)
my_gui_design.textbox_design(x=450, y=340)
my_gui_design.textbox_design(x=800, y=260)
my_gui_design.textbox_design(x=800, y=340)

#Label for Course Information
my_gui_design.label_design(x=370, y=495, text_value='Program / Course:')
my_gui_design.label_design(x=370, y=575, text_value='Year Level / Grade:')
my_gui_design.label_design(x=750, y=495, text_value='Section / Class:')
my_gui_design.label_design(x=750, y=575, text_value='Enrollment Status:')
my_gui_design.label_design(x=1100, y=495, text_value='Academic Adviser:')
my_gui_design.label_design(x=1100, y=575, text_value='Course Mode:')

#Textbox for Course Information
my_gui_design.textbox_design(x=370, y=535)
my_gui_design.textbox_design(x=370, y=615)
my_gui_design.textbox_design(x=750, y=535)
my_gui_design.textbox_design(x=750, y=615)
my_gui_design.textbox_design(x=1100, y=535)
my_gui_design.textbox_design(x=1100, y=615)

#Label for Student Information and Course Information
my_gui_design.label_design2(x=50, y=165, text_value='STUDENT INFORMATION:')
my_gui_design.label_design2(x=350, y=440, text_value='COURSE INFORMATION:')

# Adding combo for gender
n = tk.StringVar()
combo_field1 = ttk.Combobox(window, width=37, textvariable=n)
combo_field1['values'] = (' Male', 'Female')
combo_field1.place(x=450, y=341)
combo_field1.current()

# Adding combo for enrollment status
n = tk.StringVar()
combo_field1 = ttk.Combobox(window, width=37, textvariable=n)
combo_field1['values'] = (' Regular ', ' Irregular',)
combo_field1.place(x=750, y=616)
combo_field1.current()

# Adding combo for course mode
n = tk.StringVar()
combo_field1 = ttk.Combobox(window, width=37, textvariable=n)
combo_field1['values'] = (' Face to Face ', ' Online ', ' Blended ',)
combo_field1.place(x=1100, y=615)
combo_field1.current()

window.mainloop()
