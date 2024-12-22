from tkinter import *
import math

# Create the main window
root = Tk()
root.title('Simple Calculator')
root.geometry('290x520')
root.resizable(0, 0)
root.config(bg='skyblue')

# Global expression variable
expression = ""

# Update the display function
def update_display():
    rom.config(text=expression)

# Function to append digits to the expression
def append_to_expression(op):
    global expression
    expression += str(op)
    update_display()

# Function to perform operations like +, -, *, /
def perform_operation(op):
    global expression
    expression += str(op)
    update_display()

# Function to calculate the result of the expression
def calculate():
    global expression
    try:
        expression = str(eval(expression))  # Evaluates the expression
    except Exception:
        expression = "Error"
    update_display()

# Function to clear the expression
def clear_expression():
    global expression
    expression = ""
    update_display()

# Function to clear the last character
def clear_last_char():
    global expression
    expression = expression[:-1]
    update_display()

# Function to calculate percentage
def percentage():
    global expression
    try:
        expression = str(float(expression) / 100)
    except Exception:
        expression = "Error"
    update_display()

# Function to calculate square root
def square_root():
    global expression
    try:
        expression = str(float(expression) ** 0.5)
    except Exception:
        expression = "Error"
    update_display()

# Function to calculate square
def square():
    global expression
    try:
        expression = str(float(expression) ** 2)
    except Exception:
        expression = "Error"
    update_display()

# Function to calculate exponentiation (e^x)
def exponentiation():
    global expression
    try:
        expression = str(math.e ** float(expression))
    except Exception:
        expression = "Error"
    update_display()

# Function to calculate factorial
def factorial():
    global expression
    try:
        expression = str(math.factorial(int(expression)))
    except Exception:
        expression = "Error"
    update_display()

# Label to display the expression/result
rom = Label(root, text='0', bg="white", fg='black')
rom.grid(row=0, column=0, pady=20, columnspan=8, sticky='w')
rom.config(font=('verdana', 30, 'bold'))

# Button layout as a list of tuples (text, command)
buttons = [
    ('%', percentage), ('CE', clear_expression), ('C', clear_expression), ('X', clear_last_char),
    ('7', lambda: append_to_expression(7)), ('8', lambda: append_to_expression(8)), ('9', lambda: append_to_expression(9)), ('/', lambda: perform_operation('/')),
    ('4', lambda: append_to_expression(4)), ('5', lambda: append_to_expression(5)), ('6', lambda: append_to_expression(6)), ('*', lambda: perform_operation('*')),
    ('1', lambda: append_to_expression(1)), ('2', lambda: append_to_expression(2)), ('3', lambda: append_to_expression(3)), ('-', lambda: perform_operation('-')),
    ('0', lambda: append_to_expression(0)), ('.', lambda: append_to_expression('.')), ('=', calculate), ('+', lambda: perform_operation('+')),
    ('sq', square_root), ('x^2', square), ('e^x', exponentiation), ('x!', factorial)
]

# Create and place buttons dynamically
row, col = 1, 0
for (text, command) in buttons:
    button = Button(root, text=text, bg="orange" if text in ['%', '/', '*', '-', '+', '=', 'sq', 'x^2', 'e^x', 'x!'] else 'grey',
                    fg='black', width=9, height=4, command=command)
    button.grid(row=row, column=col)
    col += 1
    if col > 3:  # Move to the next row after 4 columns
        col = 0
        row += 1

# Start the main loop to display the window
root.mainloop()
