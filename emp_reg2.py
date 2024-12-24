import tkinter as tk
from emp_reg import design_gui_interface
from tkinter import ttk

#window
window = tk.Tk()
window.title('Employee Registration')
window.geometry("900x800")

#instantation of the class
obj =  design_gui_interface
my_gui_design = design_gui_interface(window)

#call for heading
my_gui_design.heading_design1(x=275, y=15, text_value="Employee's Personal Information")

#casll for frame
my_gui_design.frames1(x=50, y=80)
my_gui_design.frames1(x=50, y=220)
my_gui_design.frames2(x=50, y=380)
my_gui_design.frames3(x=50, y=520)

#call for image
upload_image = my_gui_design.image_design(image_location=r"C:\Users\Jester\Documents\GitHub\PLDL_CPE201\default.jpg", x=55, y=25, length=120, width=120)

#call for label in 1st frame
no_file_chosen = my_gui_design.label_design1(x=75, y=185, text_value="No File Chosen")
first_namelbl = my_gui_design.label_design1(x=200, y=90, text_value="First Name")
middle_namelbl = my_gui_design.label_design1(x=390, y=90, text_value="Middle Name")
last_namelbl = my_gui_design.label_design1(x=520, y=90, text_value="Last Name")
suffixlbl = my_gui_design.label_design1(x=710, y=90, text_value="Suffix")
date_of_birthlbl = my_gui_design.label_design1(x=200, y=140, text_value="Date of Birth")
genderlbl = my_gui_design.label_design1(x=420, y=140, text_value="Gender")
nationalitylbl = my_gui_design.label_design1(x=550, y=140, text_value="Nationality")
civil_statuslbl = my_gui_design.label_design1(x=680, y=140, text_value="Civil Status")

#call for textbox in 1st frame
first_nametxt = my_gui_design.textbox_design3(x=200, y=110)
middle_nametxt = my_gui_design.textbox_design1(x=390, y=110)
last_nametxt = my_gui_design.textbox_design3(x=520, y=110)
suffixtxt = my_gui_design.textbox_design1(x=710, y=110)
date_of_birthtxt = my_gui_design.textbox_design4(x=200, y=160)
gendertxt = my_gui_design.textbox_design1(x=420, y=160)
nationalitytxt = my_gui_design.textbox_design1(x=550, y=160)
civil_statustxt = my_gui_design.textbox_design2(x=680, y=160)

#call for label in 2nd frame
departmentlbl = my_gui_design.label_design1(x=75, y=230, text_value="Department")
designationlbl = my_gui_design.label_design1(x=387, y=230, text_value="Designation")
qualified_dependents_statuslbl = my_gui_design.label_design1(x=610, y=230,  text_value="Qualified Dep. Status")
employee_statuslbl = my_gui_design.label_design1(x=75, y=280, text_value="Employee Status")
pay_datelbl = my_gui_design.label_design1(x=448, y=280, text_value="Pay Date")
employee_numberlbl = my_gui_design.label_design1(x=610, y=280, text_value="Employee Number")

#call for textbox in 2nd frame
departmenttxt = my_gui_design.textbox_design5(x=75, y=250)
designationtxt = my_gui_design.textbox_design4(x=387, y=250)
qualified_dependents_statustxt = my_gui_design.textbox_design6(x=610, y=250)
employee_statustxt = my_gui_design.textbox_design7(x=75, y=300)
pay_datetxt = my_gui_design.textbox_design2(x=448, y=300)
employee_numbertxt = my_gui_design.textbox_design6(x=610, y=300)

#call for label in 3rd frame
contact_infolbl = my_gui_design.heading_design2(x=50, y=355, text_value="Contact Info:")
contat_nolbl = my_gui_design.label_design1(x=75, y=390, text_value="Contact No.")
emaillbl = my_gui_design.label_design1(x=390, y=390, text_value="Email")
otherlbl = my_gui_design.label_design1(x=75, y=435, text_value="Other(Social Media)")
soc_med_acclbl = my_gui_design.label_design1(x=390, y=435, text_value="Social Media Account ID/No.")

#call for textbox in 3rd frame
contact_notxt = my_gui_design.textbox_design5(x=75, y=410)
emailtxt = my_gui_design.textbox_design8(x=390, y=410)
othertxt = my_gui_design.textbox_design5(x=75, y=455)
soc_med_acctxt = my_gui_design.textbox_design8(x=390, y=455)

#call for label in 4th frame
addresslbl = my_gui_design.heading_design2(x=50, y=495, text_value="Address:")
add_line1lbl = my_gui_design.label_design1(x=75, y=525, text_value="Address Line 1")
add_line2lbl = my_gui_design.label_design1(x=75, y=565, text_value="Address Line 2")
city_municipalitylbl = my_gui_design.label_design1(x=75, y=605, text_value="City/Municipality")
state_provincelbl = my_gui_design.label_design1(x=458, y=605, text_value="State/Province")
countrylbl = my_gui_design.label_design1(x=75, y=643, text_value="Country")
zip_codelbl = my_gui_design.label_design1(x=458, y=643, text_value="Zip Code")
pic_path = my_gui_design.label_design1(x=75, y=680, text_value="Picture Path")


#call for textbox in 4th frame
add_line1txt = my_gui_design.textbox_design9(x=75, y=545)
add_line2txt = my_gui_design.textbox_design9(x=75, y=585)
city_municipalitytxt = my_gui_design.textbox_design10(x=75, y=625)
state_provincetxt = my_gui_design.textbox_design10(x=458, y=625)
countrytxt = my_gui_design.textbox_design10(x=75, y=663)
zip_codetxt = my_gui_design.textbox_design10(x=458, y=663)
pic_pathtxt = my_gui_design.textbox_design9(x=75, y=700)

# Adding combo for gender
n = tk.StringVar()
combo_field1 = ttk.Combobox(window, width=17, textvariable=n)
combo_field1['values'] = ('Male', 'Female')
combo_field1.place(x=420, y=160)
combo_field1.current()

# Adding combo for civil status
n = tk.StringVar()
combo_field1 = ttk.Combobox(window, width=22, textvariable=n)
combo_field1['values'] = (' Single', ' Married', ' Widow', ' Legally Separated', ' Annulled')
combo_field1.place(x=680, y=160)
combo_field1.current()

# Adding combo for nationality
n = tk.StringVar()
combo_field1 = ttk.Combobox(window, width=17, textvariable=n)
combo_field1['values'] = (' Filipino', 'Chinese', 'Indian', 'Japanese', 'Korean', 'Australian', 'Turkish', 'Iraqi', 'Italian', 'British', 'Spanish', 'Swedish', 'Dutch')
combo_field1.place(x=550, y=160)
combo_field1.current()

# Adding combo for other (social media)
n = tk.StringVar()
combo_field1 = ttk.Combobox(window, width=47, textvariable=n)
combo_field1['values'] = (' Facebook', ' Instagram', ' Twitter', 'Youtube', ' Tiktok', 'Snapchat', 'Pinterest', 'Messenger', 'Telegram', 'Twitch')
combo_field1.place(x=75, y=455)
combo_field1.current()

# Adding combo for country
n = tk.StringVar()
combo_field1 = ttk.Combobox(window, width=59, textvariable=n)
combo_field1['values'] = ('Philippines', ' Korea', ' China', 'Thailand', ' Poland', 'Vietnam', 'Portugal', 'Japan', 'United States', 'Brazil')
combo_field1.place(x=75, y=663)
combo_field1.current()

#call for button
my_gui_design.button_design1(x=63, y=150)
my_gui_design.button_design2(x=50, y=750)
my_gui_design.button_design3(x=160, y=750)

window.mainloop()
