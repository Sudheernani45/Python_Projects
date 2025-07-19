###Full Code Explanation

from tkinter import *
Imports all classes and functions from the tkinter module for GUI building.

##🔁 Global Expression Variable

expr = ""  # Global expression string
Holds the current math expression (e.g., "5+2*3").

##🔢 Append Input

def press(key):
    global expr
    expr += str(key)
    display.set(expr)
Appends the pressed key (number/operator) to the global expr.

Updates the text shown in the calculator’s input field.

##➕ Evaluate Expression

def equal():
    global expr
    try:
        result = str(eval(expr))  # Evaluate the expression
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""
eval() evaluates the string expression.

On success, shows result and clears expression.

On error (e.g., invalid input), shows "error" and clears.

##🧼 Clear Function

def clear():
    global expr
    expr = ""
    display.set("")
Clears the current expression and input field.

##🖥️ Main GUI Initialization

if __name__ == "__main__":
    root = Tk()
    root.configure(bg="light green")
    root.title("Simple Calculator")
    root.geometry("270x150")
Initializes the main application window with background color, title, and size.

##📺 Display Field

    display = StringVar()
    entry = Entry(root, textvariable=display)
    entry.grid(columnspan=4, ipadx=70)
StringVar() binds the input field to dynamically update the text.

Entry: Input field for showing expressions/results.

ipadx=70: Makes the entry field wider.

##🔢 Number Buttons (0–9)

    btn1 = Button(root, text='1', ..., command=lambda: press(1), ...)
    btn1.grid(row=2, column=0)
    ...
    btn0 = Button(root, text='0', ..., command=lambda: press(0), ...)
    btn0.grid(row=5, column=1)
Buttons for digits.

Each button calls press() with its number when clicked.

##➕➖ Multiplication & Division

    add = Button(root, text='+', ..., command=lambda: press('+'), ...)
    ...
    div = Button(root, text='/', ..., command=lambda: press('/'), ...)
Buttons for operators (+, -, *, /).

🟰 Equal, Clear, Dot

    eql = Button(root, text='equal', ..., command=equal, ...)
    clr = Button(root, text='clear', ..., command=clear, ...)
    dot = Button(root, text='.', ..., command=lambda: press('.'), ...)
equal button calls the equal() function to evaluate.

clear button resets everything.

. button allows decimal inputs.

##🌀 Event Loop

    mainloop()
Keeps the GUI running and responsive.

###✅ Features Included
Basic arithmetic: +, -, *, /

Decimal support

Clear button

Error handling

Responsive layout
