import tkinter as tk
from payroll import design_gui_interface
from tkinter import ttk

#window
window = tk.Tk()
window.title('Payroll Page')
window.geometry("900x800")

# Instantiation of the class
obj = design_gui_interface
my_gui_design = design_gui_interface(window)

# Heading for payroll
my_gui_design.heading_design1(x=260, y=20, text_value="PAYROLL CHECK")

# Label1 for employee basic info
employee_numberlbl = my_gui_design.label_design1(x=40, y=230, text_value='Employee Number')
search_employeelbl = my_gui_design.label_design1(x=40, y=270, text_value='Search Employee')
departmentlbl = my_gui_design.label_design1(x=40, y=300, text_value='Deperment')
firstname_lbl = my_gui_design.label_design1(x=450, y=80, text_value='Firstname')
middle_namelbl = my_gui_design.label_design1(x=450, y=110, text_value='Middle Name')
surnamelbl = my_gui_design.label_design1(x=450, y=140, text_value='Surname')
civil_statuslbl = my_gui_design.label_design1(x=450, y=170, text_value='Civil Status')
qualified_dependents_statuslbl = my_gui_design.label_design1(x=450, y=200, text_value='Qualified Depentents Status')
pay_datelbl = my_gui_design.label_design1(x=450, y=230, text_value='Paydate')
employee_statuslbl = my_gui_design.label_design1(x=450, y=260, text_value='Employee Status')
designationlbl = my_gui_design.label_design1(x=450, y=290, text_value='Designation')

# Textbox for employee basic info
employee_numbertxt = my_gui_design.textbox_design(x=180, y=230)
departmenttxt = my_gui_design.textbox_design2(x=180, y=300)
firstnametxt = my_gui_design.textbox_design2(x=640, y=80)
middle_nametxt = my_gui_design.textbox_design2(x=640, y=110)
surnametxt = my_gui_design.textbox_design2(x=640, y=140)
civil_statustxt = my_gui_design.textbox_design2(x=640, y=170)
qualified_dependents_statustxt = my_gui_design.textbox_design(x=640, y=200)
pay_datetxt = my_gui_design.textbox_design(x=640, y=230)
employee_statustxt = my_gui_design.textbox_design2(x=640, y=260)
designationtxt = my_gui_design.textbox_design2(x=640, y=290)

# Label1 for basic income
rate_per_hourlbl = my_gui_design.label_design1(x=40, y=360, text_value='Rate / Hour')
no_of_hours_cut_offlbl = my_gui_design.label_design1(x=40, y=390, text_value='No. of Hours / Cut Off')
income_cut_offlbl = my_gui_design.label_design1(x=40, y=420, text_value='Income / Cut Off')

# Textbox for basic income
rate_per_hourtxt = my_gui_design.textbox_design(x=180, y=360)
no_of_hours_cut_offtxt = my_gui_design.textbox_design(x=180, y=390)
income_cut_offtxt = my_gui_design.textbox_design2(x=180, y=420)

# Label1 for Honorarium income
rate_per_hourlbl = my_gui_design.label_design1(x=40, y=480, text_value='Rate / Hour')
no_of_hours_cut_offlbl = my_gui_design.label_design1(x=40, y=510, text_value='No. of Hours / Cut Off')
income_cut_offlbl = my_gui_design.label_design1(x=40, y=540, text_value='Income / Cut Off')

# Textbox for honorarium income
rate_per_hourtxt = my_gui_design.textbox_design(x=180, y=480)
no_of_hours_cut_offtxt = my_gui_design.textbox_design(x=180, y=510)
income_cut_offtxt = my_gui_design.textbox_design2(x=180, y=540)

# Label1 for other income
rate_per_hourlbl = my_gui_design.label_design1(x=40, y=600, text_value='Rate / Hour')
no_of_hours_cut_offlbl = my_gui_design.label_design1(x=40, y=630, text_value='No. of Hours / Cut Off')
income_cut_offlbl = my_gui_design.label_design1(x=40, y=660, text_value='Income / Cut Off')

# Textbox for other income
rate_per_hourtxt = my_gui_design.textbox_design(x=180, y=600)
no_of_hours_cut_offtxt = my_gui_design.textbox_design(x=180, y=630)
income_cut_offtxt = my_gui_design.textbox_design2(x=180, y=660)

# Label1 for summary income
gross_incomelbl = my_gui_design.label_design1(x=40, y=720, text_value='GROSS INCOME')
net_incomelbl = my_gui_design.label_design1(x=40, y=750, text_value='NET INCOME')

# Textbox for summary income
gross_incometxt = my_gui_design.textbox_design(x=180, y=720)
net_incometxt = my_gui_design.textbox_design2(x=180, y=750)

# Label1 for regular deductions
sss_contributionlblb = my_gui_design.label_design1(x=450, y=350, text_value='SSS Contribution')
philhealth_contributionlbl = my_gui_design.label_design1(x=450, y=380, text_value='PhilHealth Contribution')
pagibig_contributionlblb = my_gui_design.label_design1(x=450, y=410, text_value='Pagibig Contribution')
income_tax_contributiontxt = my_gui_design.label_design1(x=450, y=440, text_value='Income Tax Contribution')

# Textbox for regular deductions
sss_contributiontxt = my_gui_design.textbox_design2(x=640, y=350)
philhealth_contributiontxt = my_gui_design.textbox_design2(x=640, y=380)
pagibig_contributiontxt = my_gui_design.textbox_design2(x=640, y=410)
income_tax_contribution = my_gui_design.textbox_design2(x=640, y=440)

# Label1 for other deductions
sss_loanlbl = my_gui_design.label_design1(x=450, y=500, text_value='SSS Loan')
pagibig_loanlbl = my_gui_design.label_design1(x=450, y=530, text_value='Pagibig Loan')
faculty_savings_depositlbl = my_gui_design.label_design1(x=450, y=560, text_value='Faculty Savings Deposit')
faculty_savings_loanlbl = my_gui_design.label_design1(x=450, y=590, text_value='Faculty Savings Loan')
salary_loanlbl = my_gui_design.label_design1(x=450, y=620, text_value='Salary Loan')
other_loanlbl = my_gui_design.label_design1(x=450, y=650, text_value='Other Loan')

# Textbox for other deductions
sss_loantxt = my_gui_design.textbox_design(x=640, y=500)
pagibig_loantxt = my_gui_design.textbox_design(x=640, y=530)
faculty_savings_deposittxt = my_gui_design.textbox_design(x=640, y=560)
faculty_savings_loantxt = my_gui_design.textbox_design(x=640, y=590)
salary_loantxt = my_gui_design.textbox_design(x=640, y=620)
other_loantxt = my_gui_design.textbox_design(x=640, y=650)

# Label1 for deduction summary
total_deductionlbl = my_gui_design.label_design1(x=450, y=710, text_value='Total Deduction')

# Textbox for deduction summary
total_deductiontxt = my_gui_design.textbox_design2(x=640, y=710)

# Label2 design
employee_basic_infolbl = my_gui_design.label_design2(x=20, y=70, text_value='EMPLOYEE BASIC INFO:')
basic_incomelbl = my_gui_design.label_design2(x=30, y=330, text_value='BASIC INCOME:')
honorarium_incomelbl = my_gui_design.label_design2(x=30, y=450, text_value='HONORARIUM INCOME:')
other_incomelbl = my_gui_design.label_design2(x=30, y=570, text_value='OTHER INCOME:')
summary_incomelbl = my_gui_design.label_design2(x=30, y=690, text_value='SUMMARY INCOME:')
regular_deductionslbl = my_gui_design.label_design2(x=430, y=320, text_value='REGULAR DEDUCTIONS:')
other_deductionslbl = my_gui_design.label_design2(x=430, y=470, text_value='OTHER DEDUCTIONS:')
deduction_summarylbl = my_gui_design.label_design2(x=430, y=680, text_value='DEDUCTION SUMMARY:')

# Call for all button
uploadbutton = my_gui_design.button_design1(x=180, y=260)
uploadbutton = my_gui_design.button_design2(x=430, y=750)
uploadbutton = my_gui_design.button_design3(x=528, y=750)
uploadbutton = my_gui_design.button_design4(x=620, y=750)
uploadbutton = my_gui_design.button_design5(x=698, y=750)
uploadbutton = my_gui_design.button_design6(x=776, y=750)

# Adding combo for civil status
n = tk.StringVar()
combo_field1 = ttk.Combobox(window, width=34, textvariable=n)
combo_field1['values'] = (' Single', ' Married', ' Widow', ' Legally Separated', ' Annulled')
combo_field1.place(x=640, y=170)
combo_field1.current()

# call image to display
upload_image = my_gui_design.image_design(image_location=r"C:\Users\Jester\Documents\GitHub\PLDL_CPE201\default.jpg", x=40, y=100, length=120, width=120)

window.mainloop()