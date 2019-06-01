import tkinter as tk
from tkinter import messagebox
mainWindow = tk.Tk()
mainWindow.title("calculator")

heading_label = tk.Label(mainWindow, text='Enter first number')
heading_label.pack()
first_number_entry = tk.Entry(mainWindow)
first_number_entry.pack()

heading_label2 = tk.Label(mainWindow, text='Enter second number')
heading_label2.pack()

second_number_entry = tk.Entry(mainWindow)
second_number_entry.pack()

operations = tk.Label(mainWindow, text='Operations')
operations.pack()

def addition():
    first, second = takeValueInput()
    result = first + second
    result_label.config(text="operations result is: " + str(result))
def subtract():
    first, second = takeValueInput()
    result = first - second
    result_label.config(text="operations result is: " + str(result))
def multiply():
    first, second = takeValueInput()
    result = first * second
    result_label.config(text="operations result is: " + str(result))
def divide():
    first, second = takeValueInput()

    if second == 0:
        messagebox.showerror("Error")
    else:
        result = first / second
        result = round(result, 2)
        result_label.config(text="operations result is: " + str(result))

def takeValueInput():
    first = first_number_entry.get()
    second = second_number_entry.get()

    try:
        first = int(first)
        second = int(second)

        return first, second
    except ValueError :
        if ((len(first_number_entry.get()) == 0) or (len(second_number_entry.get()) == 0)):
            messagebox.showerror("Error", "please enter a value")
        else:
            messagebox.showerror("Error", "Enter only integer value")
        quit(0)


button1 = tk.Button(mainWindow, text='+', command=lambda : addition())
button1.pack()
button2 = tk.Button(mainWindow, text='-', command=lambda : subtract())
button2.pack()
button3 = tk.Button(mainWindow, text='*', command=lambda : multiply())
button3.pack()
button4 = tk.Button(mainWindow, text='/', command=lambda : divide())
button4.pack()

result_label = tk.Label(mainWindow, text="operation result is:")
result_label.pack()

mainWindow.mainloop()
