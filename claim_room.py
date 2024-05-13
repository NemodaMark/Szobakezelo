import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import * 
import sys
from room_management import management

# Read data from temporary file
with open(sys.argv[1], "r") as file:
    item_values = file.read().split(",")

def btnClickFunction():
    # Get values from all input boxes
    szobaszamom = item_values[0]
    nev = nev_tb.get()
    kezd = kezd_tb.get()
    veg = veg_tb.get()
    
    # Prepare user data
    user_data = (szobaszamom, nev, kezd, veg)
    
    # Call management book method
    management.book(management.reader(), user_data)

    # Inform user about booking status
    # messagebox.showinfo("Booking Status", "The booking was successful.")

    # Close the window after successful booking
    root.destroy()

root = Tk()

# This is the section of code which creates the main window
root.geometry('304x188')
root.configure(background='#F0F8FF')
root.title('Hello, I\'m the main window')


# This is the section of code which creates the a label
Label(root, text=item_values[0], bg='#F0F8FF', font=('helvetica', 12, 'normal')).place(x=7, y=8)


# This is the section of code which creates a text input box
nev_tb=Entry(root)
nev_tb.place(x=14, y=43)


# This is the section of code which creates the a label
Label(root, text='nev_lb', bg='#F0F8FF', font=('helvetica', 8, 'normal')).place(x=146, y=44)


# This is the section of code which creates a text input box
kezd_tb=Entry(root)
kezd_tb.place(x=14, y=71)


# This is the section of code which creates the a label
Label(root, text='kezd_lb', bg='#F0F8FF', font=('helvetica', 8, 'normal')).place(x=146, y=72)


# This is the section of code which creates a text input box
veg_tb=Entry(root)
veg_tb.place(x=14, y=101)


# This is the section of code which creates the a label
Label(root, text='veg_lb', bg='#F0F8FF', font=('helvetica', 8, 'normal')).place(x=146, y=101)


# This is the section of code which creates a button
Button(root, text='Foglalas', bg='#F0F8FF', font=('helvetica', 8, 'normal'), command=btnClickFunction).place(x=118, y=158)


root.mainloop()
