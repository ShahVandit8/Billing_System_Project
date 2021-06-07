from tkinter import *
import time
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import random
import os
import sys

# ========================== Window Format Start Here ========================== #

root = Tk()
root.title("HK Billing Software")                   # This is the title
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title("Billing Software")
# This is the measurement of window
root.resizable(0, 0)                                # To prevent resizing of window
root.state("zoomed")                                # This is for Full Screen
bg_color = '#3c3f41'                                # This is variable storing hex color code
root.configure(bg=bg_color)                         # This is color of background Screen
photo = PhotoImage(file="icon.png")                 # Icon of the main window
root.iconphoto(False, photo)
bg_color1 = '#1B2631'                               # This is variable storing hex color code
bg_color2 = '#626567'                               # This is variable storing hex color code
bg_color3 = '#2b2b2b'                               # This is variable storing hex color code
title_color = '#D0D3D4'                             # This is variable storing hex color code

# ========================== Window Format End Here ========================== #


# ========== Variables ========== #

clicked = StringVar()       # select category dropdown list variable
clicked1 = StringVar()      # select product dropdown list variable
qty = IntVar()              # Quantity variable
a = int(qty.get())          # Conversion of IntStr() into int()
expression = ""             # Calculator starting variable
input_text = StringVar()    # It is used to get the instance of input field

# Total and Tax variables
grocery_price = StringVar()
cosmetic_price = StringVar()
other_price = StringVar()
tax_grocery = StringVar()
tax_cosmetic = StringVar()
tax_other = StringVar()

# Customer Details Variable
cname = StringVar()
cmobile = StringVar()
billno = StringVar()
randbillno = random.randint(1000, 9000)
billno.set(str(randbillno))
search_bill = StringVar()

# Other Required Variables
items = []
quantity = []
final_price_grocery = []
final_price_cosmetic = []
final_price_other = []
final_price = []
net_amt_var = StringVar()
all_tax = StringVar()
all_total = StringVar()

# ========================== Functions Starts Here ========================== #
# Function = clock() : This will show current time
def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    show_time.config(text=hour + ':' + minute + ':' + second)
    show_time.after(1000, clock)

# Function = Display_date()  :  This will show current date
def display_date():
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    show_date.config(text=date + '-' + month + '-' + year)
    show_date.after(1000, clock)

# Function = select_categories : This will update the product list
def select_categories(e):
    if clicked.get() == 'Groceries':
        product_drop.config(value=grocery_product)
    elif clicked.get() == 'Cosmetics':
        product_drop.config(value=cosmetic_product)
    elif clicked.get() == 'Others':
        product_drop.config(value=other_product)

# 'extra' function :  This Function continuously updates the input field whenever you enters a number
def extra(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 'clear' function : This is used to clear the input field
def clear():
    global expression
    expression = ""
    input_text.set("")

# 'evaluation':This method calculates the expression present in input field
def evaluation():
    global expression
    result = str(eval(expression))
    input_text.set(result)

# clear the selected item
def clear_crt():
    categories_drop.set(" ")
    product_drop.set(" ")
    qty.set(0)

# Append the item in cart
def add_cart():
    if clicked.get() == '':
        messagebox.showinfo("Warning", "Please Select Category")
    elif clicked1.get() == '':
        messagebox.showinfo("Warning", "Please Select Product")
    # elif a == 0:
    #     messagebox.showinfo("Warning", "Please Enter the Quantity")
    elif qty.get() == 0:
        messagebox.showinfo("Warning", "Please Enter the Quantity")
    elif clicked1.get() == 'Rice':
        items.append(clicked1.get())
        quantity.append(qty.get())
        price = qty.get() * 50
        final_price_grocery.append(price)
        final_price.append(price)
    elif clicked1.get() == 'Wheat':
        items.append(clicked1.get())
        quantity.append(qty.get())
        price = qty.get() * 70
        final_price_grocery.append(price)
        final_price.append(price)
    elif clicked1.get() == 'Sugar':
        items.append(clicked1.get())
        quantity.append(qty.get())
        price = qty.get() * 150
        final_price_grocery.append(price)
        final_price.append(price)
    elif clicked1.get() == 'Oil':
        items.append(clicked1.get())
        quantity.append(qty.get())
        price = qty.get() * 120
        final_price_grocery.append(price)
        final_price.append(price)
    elif clicked1.get() == 'Soap':
        items.append(clicked1.get())
        quantity.append(qty.get())
        price = qty.get() * 100
        final_price_cosmetic.append(price)
        final_price.append(price)
    elif clicked1.get() == 'Cream':
        items.append(clicked1.get())
        quantity.append(qty.get())
        price = qty.get() * 180
        final_price_cosmetic.append(price)
        final_price.append(price)
    elif clicked1.get() == 'Face Wash':
        items.append(clicked1.get())
        quantity.append(qty.get())
        price = qty.get() * 300
        final_price_cosmetic.append(price)
        final_price.append(price)
    elif clicked1.get() == 'Body Wash':
        items.append(clicked1.get())
        quantity.append(qty.get())
        price = qty.get() * 250
        final_price_cosmetic.append(price)
        final_price.append(price)
    elif clicked1.get() == 'Waffers':
        items.append(clicked1.get())
        quantity.append(qty.get())
        price = qty.get() * 30
        final_price_other.append(price)
        final_price.append(price)
    elif clicked1.get() == 'Biscuits':
        items.append(clicked1.get())
        quantity.append(qty.get())
        price = qty.get() * 50
        final_price_other.append(price)
        final_price.append(price)
    elif clicked1.get() == 'Cold Drink':
        items.append(clicked1.get())
        quantity.append(qty.get())
        price = qty.get() * 30
        final_price_other.append(price)
        final_price.append(price)
    elif clicked1.get() == 'Namkeen':
        items.append(clicked1.get())
        quantity.append(qty.get())
        price = qty.get() * 80
        final_price_other.append(price)
        final_price.append(price)
    clear_crt()

# Clear All Function
def clear_all():
    items.clear()
    quantity.clear()
    final_price_grocery.clear()
    final_price_cosmetic.clear()
    final_price_other.clear()
    cosmetic_price.set("")
    grocery_price.set("")
    other_price.set("")
    tax_other.set("")
    tax_cosmetic.set("")
    tax_grocery.set("")
    net_amt_var.set("")
    cname.set("")
    cmobile.set("")
    search_bill.set("")
    billno.set("")
    randbillno = random.randint(1000, 9000)
    billno.set(str(randbillno))
    bill_txt()

# Display the Total category wise price and Tax
def display_total():
    total = 0
    total1 = 0
    total2 = 0
    final_total = 0
    for i in range(0, len(final_price_grocery)):
        total = total + final_price_grocery[i]
    grocery_price.set(str(total))

    for j in range(0, len(final_price_cosmetic)):
        total1 = total1 + final_price_cosmetic[j]
    cosmetic_price.set(str(total1))

    for k in range(0, len(final_price_other)):
        total2 = total2 + final_price_other[k]
    other_price.set(str(total2))

    grocery_after_tax = (total * 18)/100
    tax_grocery.set(grocery_after_tax)

    cosmetic_after_tax = (total1 * 22)/100
    tax_cosmetic.set(cosmetic_after_tax)

    other_after_tax = (total2 * 18)/100
    tax_other.set(other_after_tax)

    total_price = total + total1 + total2
    all_total.set(total_price)

    total_tax = grocery_after_tax + cosmetic_after_tax + other_after_tax
    all_tax.set(total_tax)

    final_total = total + grocery_after_tax + total1 + cosmetic_after_tax + total2 + other_after_tax
    final_total1 = "Rs. " + str(final_total)
    net_amt_var.set(final_total1)

# Function for Bill Area Default Text
def bill_txt():
    da = time.strftime("%d-%m-%y")
    ti = time.strftime("%H:%M")
    txtarea.delete(1.0, END)
    txtarea.insert(END, "################ Welcome to HK Retails ###############\n")
    txtarea.insert(END, "         Phone No: 9825323396 , Vadodara GJ-390018")
    txtarea.insert(END, f"\n\n Bill No: {billno.get()}\t\t\t\tDate : {da}")
    txtarea.insert(END, f"\n Customer Name: {cname.get()}\t\t\t\tTime : {ti}")
    txtarea.insert(END, f"\n Customer Phone: {cmobile.get()}")
    txtarea.insert(END, "\n######################################################")
    txtarea.insert(END, "\n    Products             Quantity             Price")
    txtarea.insert(END, "\n######################################################")

# Function bill_area : This will generate the bill
def bill_area():
    if cname.get() == '':
        messagebox.showinfo("warning", "Please enter Customer Details")
    elif cmobile.get() == '':
        messagebox.showinfo("warning", "Please enter Customer Details")
    elif not items:
        messagebox.showinfo("warning", "Please enter Products in cart")
    elif grocery_price.get() == '0' and cosmetic_price.get() == '0' and other_price.get() == '0':
        messagebox.showinfo("warning", "Please enter Products in cart")
    else:
        bill_txt()

        x = len(items)
        v = 0
        while v < x:
            txtarea.insert(END, f"\n    {items[v]}\t\t\t    {quantity[v]}\t\t\t{final_price[v]}")
            v = v + 1
        txtarea.insert(END, "\n******************************************************")
        txtarea.insert(END, f"\n    Total Price  :                              {all_total.get()}")
        txtarea.insert(END, f"\n    Total Tax :                                 {all_tax.get()}")
        txtarea.insert(END, "\n******************************************************")
        txtarea.insert(END, f"\n    Net Price  :                            {net_amt_var.get()}")
        save_bill()

# Function to Save bill Txt file in Folder
def save_bill():
    msg = messagebox.askyesno("Save Bill", "Do you want to save bill ?")
    if msg > 0:
        data_bill = txtarea.get('1.0', END)
        f1 = open("Bill_records/" + str(billno.get()) + ".txt", "w")
        f1.write(data_bill)
        f1.close()
        messagebox.showinfo("Saved", f"Bill with bill no {billno.get()} has saved successfully")
    else:
        return

# Function to Search Bill
def bill_search():
    current = "False"
    for i in os.listdir("Bill_records/"):
        if i.split('.')[0] == search_bill.get():
            f1 = open(f"Bill_records/{i}", "r")
            txtarea.delete('1.0', END)
            for j in f1:
                txtarea.insert(END, j)
            f1.close()
            current = "True"
    if current == "False":
        messagebox.showinfo("Error", "No Record Found !")

# Function to exit
def exit_window():
    msg1 = messagebox.askyesno("System", "Do you want to exit ?")
    if msg1 > 0:
        sys.exit()
    else:
        return

# ========================== Functions End Here ========================== #

# ========================== Software Design Starts Here ========================== #
# =============== Title Frame =============== #
# Top Frame 1
frame1 = Frame(root, bg=bg_color, height=50, relief=RIDGE)
frame1.pack(side=TOP, fill='x')

# Image of Clock
clock_img = Image.open("clock.png")
clock_img = clock_img.resize((30, 30))
my_clock = ImageTk.PhotoImage(clock_img)

# Clock Image Label
clock_frame = Frame(frame1, bg=bg_color)
clock_frame.pack(side=LEFT)
clockLabel = Label(clock_frame, image=my_clock, bg=bg_color, fg='white')
clockLabel.pack(side=LEFT, padx=20)

# Time display
show_time = Label(clock_frame, text='', bg=bg_color, fg='white', font='Helvetica 15 bold')
show_time.pack(side=LEFT)

# Image of Calander
calander_img = Image.open("calander.png")
calander_img = calander_img.resize((23, 23))
my_calander = ImageTk.PhotoImage(calander_img)

# Calander Image Label
date_frame = Frame(frame1, bg=bg_color)
date_frame.pack(side=RIGHT)
calanderLabel = Label(date_frame, image=my_calander, bg=bg_color, fg='white')
calanderLabel.pack(side=LEFT)

# Date Display
show_date = Label(date_frame, text='', bg=bg_color, fg='white', font='Helvetica 15 bold')
show_date.pack(side=RIGHT, padx=25)

# Image of LOGO
logo = Image.open("icon.png")
logo = logo.resize((48, 48))
my_logo = ImageTk.PhotoImage(logo)

# Logo Image Label
title_frame = Frame(frame1, bg=bg_color)
title_frame.pack(side=TOP)
logoLabel = Label(title_frame, image=my_logo, bg=bg_color, fg='white')
logoLabel.pack(side=LEFT)

# Title in Frame 1
title = Label(title_frame, text="HK Billing Software", font="Fira_Mono 30 bold", bg=bg_color, fg='white')
title.pack(side=RIGHT)

# =============== Customer Details Frame =============== #
# Frame 2 :
frame2 = LabelFrame(root, text="Customer Details", font='Helvetica 13 bold', fg=title_color, bg=bg_color)
frame2.pack(side=TOP)

# Customer Name Label
cname_label = Label(frame2, text="Customer Name: ", font="Fira_Mono 16 bold", bg=bg_color, fg='white')
cname_label.grid(row=0, column=0, padx=25, pady=20)

# Customer Name Input Field
cname_inp = Entry(frame2, width=22, font='Arial 15', textvariable=cname)
cname_inp.grid(row=0, column=1, pady=5, padx=2)

# Customer Phone Number Label
cmobile_label = Label(frame2, text="Phone No: ", font="Fira_Mono 16 bold", bg=bg_color, fg='white')
cmobile_label.grid(row=0, column=2, padx=25, pady=10)

# Customer Phone Number Input Field
cmobile_inp = Entry(frame2, width=22, font='Arial 15', textvariable=cmobile)
cmobile_inp.grid(row=0, column=3, pady=5, padx=2)

# Bill Number Label
billno_label = Label(frame2, text="Bill No: ", font="Fira_Mono 16 bold", bg=bg_color, fg='white')
billno_label.grid(row=0, column=4, padx=25, pady=10)

# Bill Number Input Field
billno_inp = Entry(frame2, width=22, font='Arial 15', textvariable=search_bill)
billno_inp.grid(row=0, column=5, pady=5, padx=2)

# Button of Bill Search
bill_button = Button(frame2, text='Search', width=15, font="Helvetica 10 bold", command=bill_search)
bill_button.grid(row=0, column=6, pady=7, padx=73)


# =============== Item Details Frame =============== #
# Frame Main
main_frame = Frame(root, bg=bg_color)
main_frame.pack(side=TOP)

# Frame 3
frame3 = LabelFrame(main_frame, text='Item Details', font='Helvetica 13 bold', fg=title_color, bg=bg_color)
frame3.pack(side=LEFT)

# Select Categories Label
categories_label = Label(frame3, text="Select Category: ", font="Fira_Mono 16 bold", bg=bg_color, fg='white')
categories_label.grid(row=0, column=0, padx=25, pady=55)

# Categories Option List and Drop Down list
categories_drop = ttk.Combobox(frame3, width=37, textvariable=clicked)
categories_drop['values'] = ("Groceries", "Cosmetics", "Others")
categories_drop.grid(row=0, column=1, padx=2, pady=5)
categories_drop.bind("<<ComboboxSelected>>", select_categories)

# Select Product Label
product_label = Label(frame3, text="Select Product: ", font="Fira_Mono 16 bold", bg=bg_color, fg='white')
product_label.grid(row=1, column=0, padx=25, pady=25)

# Product Option List and Drop Down list
grocery_product = ["Rice", "Wheat", "Sugar", "Oil"]
cosmetic_product = ["Soap", "Cream", "Face Wash", "Body Wash"]
other_product = ["Waffers", "Biscuits", "Cold Drink", "Namkeen"]
product_drop = ttk.Combobox(frame3, width=37, textvariable=clicked1, value=[" "])
product_drop.grid(row=1, column=1, padx=2, pady=25)

# Quantity Label
quantity_label = Label(frame3, text='Quantity: ', font="Fira_Mono 16 bold", bg=bg_color, fg='white')
quantity_label.grid(row=2, column=0, padx=25, pady=50)

# Quantity Input Field
quantity_inp = Entry(frame3,  width=22, font='Arial 15', textvariable=qty)
quantity_inp.grid(row=2, column=1, padx=25, pady=50)

# Add to Cart Button
atc_button = Button(frame3, text='Add To Card', width=18, font="Helvetica 13 bold", command=add_cart)
atc_button.grid(row=3, column=0, padx=25, pady=35)

# Clear Cart Button
clearct_button = Button(frame3, text='Clear', width=18, font="Helvetica 13 bold", command=clear_crt)
clearct_button.grid(row=3, column=1, padx=25, pady=35)


# =============== Calculator Frame =============== #
# Frame 4
frame4 = LabelFrame(main_frame, text='Calculator', font='Helvetica 13 bold', fg=title_color, bg=bg_color)
frame4.pack(side=LEFT)

# Let us creating a frame for the input field
input_frame = Frame(frame4, width=100, height=100, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)

# Let us create a input field inside the 'Frame'
input_field = Entry(input_frame, font=('arial', 24, 'bold'), textvariable=input_text, width=27, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=37)

# Let us creating another 'Frame' for the button below the 'input_frame'
button_frame = Frame(frame4, width=312, height=272.5, bg="grey")
button_frame.pack()

# first row
seven = Button(button_frame, text="7", fg="black", width=16, height=5, bd=0, bg="#fff", command=lambda: extra(7))
seven.grid(row=1, column=0, padx=1, pady=1)

eight = Button(button_frame, text="8", fg="black", width=16, height=5, bd=0, bg="#fff", command=lambda: extra(8))
eight.grid(row=1, column=1, padx=1, pady=1)

nine = Button(button_frame, text="9", fg="black", width=16, height=5, bd=0, bg="#fff", command=lambda: extra(9))
nine.grid(row=1, column=2, padx=1, pady=1)

multiply = Button(button_frame, text="*", fg="black", width=17, height=5, bd=0, bg="#eee", command=lambda: extra("*"))
multiply.grid(row=1, column=3, padx=1, pady=1)

# second row
four = Button(button_frame, text="4", fg="black", width=16, height=5, bd=0, bg="#fff", command=lambda: extra(4))
four.grid(row=2, column=0, padx=1, pady=1)

five = Button(button_frame, text="5", fg="black", width=16, height=5, bd=0, bg="#fff", command=lambda: extra(5))
five.grid(row=2, column=1, padx=1, pady=1)

six = Button(button_frame, text="6", fg="black", width=16, height=5, bd=0, bg="#fff", command=lambda: extra(6))
six.grid(row=2, column=2, padx=1, pady=1)

minus = Button(button_frame, text="-", fg="black", width=17, height=5, bd=0, bg="#eee", command=lambda: extra("-"))
minus.grid(row=2, column=3, padx=1, pady=1)

# third row
one = Button(button_frame, text="1", fg="black", width=16, height=5, bd=0, bg="#fff", command=lambda: extra(1))
one.grid(row=3, column=0, padx=1, pady=1)

two = Button(button_frame, text="2", fg="black", width=16, height=5, bd=0, bg="#fff", command=lambda: extra(2))
two.grid(row=3, column=1, padx=1, pady=1)

three = Button(button_frame, text="3", fg="black", width=16, height=5, bd=0, bg="#fff", command=lambda: extra(3))
three.grid(row=3, column=2, padx=1, pady=1)

plus = Button(button_frame, text="+", fg="black", width=17, height=5, bd=0, bg="#eee", command=lambda: extra("+"))
plus.grid(row=3, column=3, padx=1, pady=1)

# fourth row
Bclear = Button(button_frame, text="C", fg="black", width=16, height=5, bd=0, bg="#eee", command=lambda: clear())
Bclear.grid(row=4, column=0, padx=1, pady=1)

zero = Button(button_frame, text="0", fg="black", width=16, height=5, bd=0, bg="#fff", cursor="hand2",
              command=lambda: extra(0))
zero.grid(row=4, column=1, padx=1, pady=1)

divide = Button(button_frame, text="/", fg="black", width=16, height=5, bd=0, bg="#eee", command=lambda: extra("/"))
divide.grid(row=4, column=2, padx=1, pady=1)

equals = Button(button_frame, text="=", fg="black", width=17, height=5, bd=0, bg="#eee", cursor="hand2",
                command=lambda: evaluation())
equals.grid(row=4, column=3, padx=1, pady=1)

# =============== Bill Frame =============== #
# frame 5
frame5 = Frame(main_frame, bd=5, relief=GROOVE)
frame5.pack(side=RIGHT, padx=15, ipady=5, fill='y')

# Bill Title Label
bill_title = Label(frame5, text='Bill Area', font='arial 15 bold', bd=5, relief=GROOVE)
bill_title.pack(fill='x')

# Text Area And Scrollbar
scroll_y = Scrollbar(frame5, orient=VERTICAL)
txtarea = Text(frame5, yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT, fill='y')
scroll_y.config(command=txtarea.yview)
txtarea.pack(fill=BOTH, expand=1)

# =============== Total and Tax Frame =============== #
# Frame 6
full_frame = LabelFrame(root, text='Bill Options', font='Helvetica 13 bold', fg=title_color, bg=bg_color)
full_frame.pack(side=BOTTOM, fill='x', pady=15)
frame6 = Frame(full_frame, bg=bg_color)
frame6.pack(side=LEFT)

# Total Grocery Label
total_grocery = Label(frame6, text='Total Groceries: ', font="Fira_Mono 15 bold", bg=bg_color, fg='white')
total_grocery.grid(row=0, column=0, padx=20, pady=10, sticky='w')

# Total Grocery Text field
total_grocery_txt = Entry(frame6, width=15, font="Fira_Mono 16 bold",  textvariable=grocery_price)
total_grocery_txt.grid(row=0, column=1, padx=5, pady=10)

# Total Cosmetics Label
total_cosmetic = Label(frame6, text='Total Cosmetics: ', font="Fira_Mono 15 bold", bg=bg_color, fg='white')
total_cosmetic.grid(row=1, column=0, padx=20, pady=10, sticky='w')

# Total cosmetic Text field
total_cosmetic_txt = Entry(frame6, width=15, font="Fira_Mono 16 bold", textvariable=cosmetic_price)
total_cosmetic_txt.grid(row=1, column=1, padx=5, pady=10)

# Total Other Label
total_other = Label(frame6, text='Total Other: ', font="Fira_Mono 15 bold", bg=bg_color, fg='white')
total_other.grid(row=2, column=0, padx=20, pady=10, sticky='w')

# Total Other Text field
total_other_txt = Entry(frame6, width=15, font="Fira_Mono 16 bold", textvariable=other_price)
total_other_txt.grid(row=2, column=1, padx=5, pady=10)

# Grocery Tax Label
grocery_tax = Label(frame6, text='Groceries Tax: ', font="Fira_Mono 15 bold", bg=bg_color, fg='white')
grocery_tax.grid(row=0, column=2, padx=60, pady=10, sticky='w')

# Grocery Tax Text field
grocery_tax_txt = Entry(frame6, width=15, font="Fira_Mono 16 bold", textvariable=tax_grocery)
grocery_tax_txt.grid(row=0, column=3, padx=5, pady=10)

# Cosmetic Tax Label
cosmetic_tax = Label(frame6, text='Cosmetics Tax: ', font="Fira_Mono 15 bold", bg=bg_color, fg='white')
cosmetic_tax.grid(row=1, column=2, padx=60, pady=10, sticky='w')

# Total cosmetic Text field
cosmetic_tax_txt = Entry(frame6, width=15, font="Fira_Mono 16 bold", textvariable=tax_cosmetic)
cosmetic_tax_txt.grid(row=1, column=3, padx=5, pady=10)

# Other Tax Label
other_tax = Label(frame6, text='Other Tax: ', font="Fira_Mono 15 bold", bg=bg_color, fg='white')
other_tax.grid(row=2, column=2, padx=60, pady=10, sticky='w')

# Other Tax Text field
other_tax_txt = Entry(frame6, width=15, font="Fira_Mono 16 bold", textvariable=tax_other)
other_tax_txt.grid(row=2, column=3, padx=5, pady=10)

# =============== Net Payable Frame =============== #
# Frame 7
frame8 = Frame(full_frame, relief=GROOVE, bg=bg_color)
frame8.pack(side=LEFT)

# Net Amount Label
net_amt = Label(frame8, text='Net Amount', font="Fira_Mono 15 bold", bg=bg_color, fg='white')
net_amt.grid(row=0, column=0, padx=50, pady=15)

# Net amount Text field
net_amt_txt = Entry(frame8, width=15, font="Fira_Mono 16 bold", textvariable=net_amt_var)
net_amt_txt.grid(row=1, column=0, padx=5, pady=2)


# =============== Button Frame =============== #
# Frame 7
frame7 = Frame(full_frame, relief=GROOVE, bg=bg_color)
frame7.pack(side=RIGHT, padx=25)

# Total Button
total_button = Button(frame7, text='Total', width=16, height=3, font="Helvetica 10 bold", bg=bg_color3, fg='white', command=display_total)
total_button.grid(row=0, column=0, padx=5)

# Generate Bill Button
generatebill_button = Button(frame7, text='Generate Bill', width=16, height=3, font="Helvetica 10 bold", bg=bg_color3, fg='white', command=bill_area)
generatebill_button.grid(row=0, column=1, padx=15, pady=5)

# Clear Button
clear_button = Button(frame7, text='Clear', width=16, height=3, font="Helvetica 10 bold", bg=bg_color3, fg='white', command=clear_all)
clear_button.grid(row=1, column=0, padx=25)

# Exit Button
exit_button = Button(frame7, text='Exit', width=16, height=3, font="Helvetica 10 bold", bg=bg_color3, fg='white', command=exit_window)
exit_button.grid(row=1, column=1, padx=5)


# Calling Funtions Starts Here #
bill_txt()              # Calling bill_txt to print default Bill Data
display_date()          # Calling display_date to show date at top right
clock()                 # Calling clock to show current time at top left

root.mainloop()
