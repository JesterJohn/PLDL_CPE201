import tkinter as tk
from log_in_page import design_gui_interface

# Create main application window
window = tk.Tk()
window.title("Login Page")
window.geometry('1590x800')

# Instantiate design class
obj = design_gui_interface
my_gui_design = design_gui_interface(window)

#call for image
my_gui_design.image_design(image_location=r"C:\Users\Jester\Documents\GitHub\PLDL_CPE201\WR.jpg", x=0, y=0, length=1590, width=800)

#call for frame
my_gui_design.frames(x=556, y=150)

#call for heading
sign_inlbl = my_gui_design.heading_design(x=730, y=200, text_value='Sign-in')

#call for label
usernamelbl = my_gui_design.label_design(x=610, y=260, text_value='Username')
passwordlbl = my_gui_design.label_design(x=610, y=320, text_value='Password')
stay_signed_inlbl = my_gui_design.label_design(x=610, y=420, text_value='Stay signed in')
cant_sign_inlbl = my_gui_design.label_design(x=734, y=570, text_value="CAN'T SIGN IN")
create_accountlbl = my_gui_design.label_design(x=719, y=600, text_value="CREATE ACCOUNT")

#call for textbox
usernametxt = my_gui_design.textbox_design(x=610, y=290)
passwordtxt = my_gui_design.textbox_design(x=610, y=350)

#call for button
facebookbtn = my_gui_design.button_design1(x=610, y=380)
googlebtn = my_gui_design.button_design2(x=729, y=380)
applebtn = my_gui_design.button_design3(x=845, y=380)
loginbtn = my_gui_design.button_design4(x=729, y=530)

window.mainloop()