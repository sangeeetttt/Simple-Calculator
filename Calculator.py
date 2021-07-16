from tkinter import *

root = Tk()

root.title('Calculator')
root.config(bg='black')
root.iconbitmap("calculator.ico")
root.resizable(0,0)


#the texting space:

entryy = Entry(root, font=('arial',20,'bold'), width= '20',borderwidth= '5',  bg= 'yellow', fg= 'green', justify= 'right')
entryy.grid(row='0', column='0', columnspan='4', padx='5', pady='10',)


# functions:

# for clicking numbers:
def button_click(number):
    current = entryy.get()
    entryy.delete(0, END)
    entryy.insert(0, str(current)+str(number))

# for clear button:
def button_clear():
    entryy.delete(0,END)

# for add button:
def button_addition():
    value_first= entryy.get()
    global first_value
    global math
    math= 'addition'
    first_value= int(value_first)
    entryy.delete(0, END)

# for equal button:
def button_equal():
    second_value = entryy.get()
    entryy.delete(0,END)

    if math == "addition":
        entryy.insert(0, first_value + int(second_value))

    if math == "substraction":
        entryy.insert(0, first_value - int(second_value))

    if math == "multiplication":
        entryy.insert(0, first_value * int(second_value))

    if math == "division":
        entryy.insert(0, first_value / int(second_value))

# for subtraction button:
def button_subtraction():
    value_first= entryy.get()
    global first_value
    global math
    math= 'substraction'
    first_value = int(value_first)
    entryy.delete(0, END)

# for division:
def button_divide():
    value_first= entryy.get()
    global first_value
    global math
    math= 'division'
    first_value= int(value_first)
    entryy.delete(0, END)

#for multiplication:
def button_multiply():
    value_first= entryy.get()
    global first_value
    global math
    math= 'multiplication'
    first_value= int(value_first)
    entryy.delete(0, END)





# Defining buttons as numbers:

button1 = Button(root, width='11', height='4', bd='0', text='1', bg = 'black', fg= 'yellow', command=lambda : button_click(1))
button2 = Button(root, width='11', height='4', bd='0', text='2', bg = 'black', fg= 'yellow', command=lambda : button_click(2))
button3 = Button(root, width='11', height='4', bd='0', text='3', bg = 'black', fg= 'yellow', command=lambda : button_click(3))
button4 = Button(root, width='11', height='4', bd='0', text='4', bg = 'black', fg= 'yellow', command=lambda : button_click(4))
button5 = Button(root, width='11', height='4', bd='0', text='5', bg = 'black', fg= 'yellow', command=lambda : button_click(5))
button6 = Button(root, width='11', height='4', bd='0', text='6', bg = 'black', fg= 'yellow', command=lambda : button_click(6))
button7 = Button(root, width='11', height='4', bd='0', text='7', bg = 'black', fg= 'yellow', command=lambda : button_click(7))
button8 = Button(root, width='11', height='4', bd='0', text='8', bg = 'black', fg= 'yellow', command=lambda : button_click(8))
button9 = Button(root, width='11', height='4', bd='0', text='9', bg = 'black', fg= 'yellow', command=lambda : button_click(9))
button0 = Button(root, width='11', height='4', bd='0', text='0', bg = 'black', fg= 'yellow', command=lambda : button_click(0))

button_add = Button(root, width='11', height='4', bd='0', text='+', bg= 'black', fg='blue' , command=button_addition)
button_sub = Button(root, width='11', height='4', bd='0', text='-', bg= 'black', fg='blue' , command=button_subtraction)
button_mul = Button(root, width='11', height='4', bd='0', text='*', bg= 'black', fg='blue' , command=button_multiply)
button_div = Button(root, width='11', height='4', bd='0', text='/', bg= 'black', fg='blue' , command=button_divide)
button_clr = Button(root, width='11', height='4', bd='0', text='clr', bg= 'black', fg='red', command=button_clear)
button_eql = Button(root, width='11', height='4', bd='0', text='=', bg= 'black', fg='white', command=button_equal)


# Placing buttons for numbers:

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)

# Placing Buttons for signs:

button_add.grid(row=4,column=1)
button_eql.grid(row=4,column=3)
button_clr.grid(row=1,column=3)
button_div.grid(row=2,column=3)
button_mul.grid(row=3,column=3)
button_sub.grid(row=4,column=2)


root.mainloop()