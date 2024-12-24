import tkinter as tk
from user_acc_info import design_gui_interface

window = tk.Tk()
window.title("User Account Information")
window.geometry('900x500')

# Instantiate the design class
obj = design_gui_interface
my_gui_design = design_gui_interface(window)

# Call heading
my_gui_design.heading_design(x=40, y=30, text_value="User Account Information")

# Call frame
my_gui_design.frames(x=40, y=150)

# Call image to display
my_gui_design.image_design(image_location=r"C:\Users\Jester\Documents\GitHub\PLDL_CPE201\default.jpg", x=45, y=80, length=150, width=150,)

# Call labels
firstnamelbl = my_gui_design.label_design(x=220, y=165, text_value='First Name')
middle_namelbl = my_gui_design.label_design(x=340, y=165, text_value='Middle Name')
last_namelbl = my_gui_design.label_design(x=485, y=165, text_value='Last Name')
suffixlbl = my_gui_design.label_design(x=605, y=165, text_value='Suffix')
departmentlbl = my_gui_design.label_design(x=725, y=165, text_value='Department')
designationlbl = my_gui_design.label_design(x=60, y=250, text_value='Designation')
usernamelbl = my_gui_design.label_design(x=340, y=250, text_value='Username')
passwordlbl = my_gui_design.label_design(x=530, y=250, text_value='Password')
confirm_passwordlbl = my_gui_design.label_design(x=60, y=320, text_value='Confirm Password')
user_typelbl = my_gui_design.label_design(x=340, y=320, text_value='User Type')
user_status = my_gui_design.label_design(x=530, y=320, text_value='User Status')
employee_number = my_gui_design.label_design(x=673, y=320, text_value='Employee Number')

# Call textboxes
first_nametxt = my_gui_design.textbox_design2(x=220, y=190)
middle_nametxt = my_gui_design.textbox_design3(x=340, y=190)
last_nametxt = my_gui_design.textbox_design2(x=485, y=190)
suffixtxt = my_gui_design.textbox_design2(x=605, y=190)
departmenttxt = my_gui_design.textbox_design2(x=725, y=190)
designationtxt = my_gui_design.textbox_design4(x=60, y=275)
usernametxt = my_gui_design.textbox_design(x=340, y=275)
passwordtxt = my_gui_design.textbox_design5(x=530, y=275)
confirm_passwordtxt = my_gui_design.textbox_design5(x=60, y=345)
user_typetxt = my_gui_design.textbox_design(x=340, y=345)
user_statustxt = my_gui_design.textbox_design6(x=530, y=345)
employee_numbetxt = my_gui_design.textbox_design6(x=673, y=345)

# Call buttons
my_gui_design.button_design1(x=250, y=390)
my_gui_design.button_design2(x=360, y=390)
my_gui_design.button_design3(x=470, y=390)

# Start the main loop
window.mainloop()
