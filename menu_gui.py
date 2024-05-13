import tkinter as tk
from tkinter import ttk
from room_management import management
import subprocess

def open_screen(screen):
    # Hide the current screen
    main_menu_frame.pack_forget()
    
    # Show the selected screen
    screen.pack()

def back_to_main_menu(current_screen):
    # Hide the current screen
    current_screen.pack_forget()
    
    # Show the main menu
    main_menu_frame.pack()

def button_click(row):
    print(f"Button clicked for item {row}")  # Replace with your action

def show_all_rooms():
    show_rooms(claimed_filter=None)

def show_non_claimed_rooms():
    show_rooms(claimed_filter=0)

def show_claimed_rooms():
    show_rooms(claimed_filter=1)

def show_rooms(claimed_filter=None):
    # Clear existing data in tables
    all_rooms = management.reader()
    table = []
    unclaimed_table = []
    claimed_table = []

    # Show all rooms in the first table
    for room in all_rooms:
        if claimed_filter == 1 and room.claimed == "1":
            claimed_table.append((room.id, room.beds, room.price, room.vip, room.claimed, room.start_date, room.end_date, room.claimer_name))
        elif claimed_filter == 0 and room.claimed == "0":
            unclaimed_table.append((room.id, room.beds, room.price, room.vip, room.claimed, room.start_date, room.end_date, room.claimer_name))
        else:
            table.append((room.id, room.beds, room.price, room.vip, room.claimed, room.start_date, room.end_date, room.claimer_name))
            
    # Clear existing data in tables
    for item in table_tree.get_children():
        table_tree.delete(item)
    for item in table_non_claimed_tree.get_children():
        table_non_claimed_tree.delete(item)
    for item in table_claimed_tree.get_children():
        table_claimed_tree.delete(item)

    # Insert rows into the tables
    for row in table:
        table_tree.insert("", "end", values=row)
    for row in unclaimed_table:
        table_non_claimed_tree.insert("", "end", values=row)
    for row in claimed_table:
        table_claimed_tree.insert("", "end", values=row)

def on_tree_click(event):
    item = event.widget.selection()[0]  # Get selected item
    item_values = event.widget.item(item, "values")  # Get values of selected item
    print("Clicked item:", item_values)
    if item_values[6] == " ":
        open_claim_room(item_values)
    else:
        # Extract the room number from item_values
        room_number = item_values[0]
        # Pass room_number as a string to the cancel method
        management.cancel(management.reader(), room_number)

def open_claim_room(item_values):
    # Write room data to a temporary file
    with open("temp_room_data.txt", "w") as file:
        file.write(",".join(item_values))
    
    # Open claim_room.py with the temporary file
    subprocess.Popen(["python", "claim_room.py", "temp_room_data.txt"])

# Main Menu
root = tk.Tk()
root.title("Main Menu")
root.geometry("1600x500")  # Set initial window size

main_menu_frame = tk.Frame(root)
main_menu_frame.pack(pady=20)

label = tk.Label(main_menu_frame, text="Main Menu", font=("Helvetica", 18))
label.pack(pady=10)

button1 = tk.Button(main_menu_frame, text="Elfoglalt szobák", command=show_non_claimed_rooms)
button1.pack(pady=5)

button2 = tk.Button(main_menu_frame, text="Szabad szobák", command=show_claimed_rooms)
button2.pack(pady=5)

button3 = tk.Button(main_menu_frame, text="Összes szoba", command=show_all_rooms)
button3.pack(pady=5)

# Screen 1
screen1_frame = tk.Frame(root)

label_screen1 = tk.Label(screen1_frame, text="Non-Claimed Rooms", font=("Helvetica", 18))
label_screen1.pack(pady=10)

back_button1 = tk.Button(screen1_frame, text="Back to Main Menu", command=lambda: back_to_main_menu(screen1_frame))
back_button1.pack(pady=5)

# Screen 2
screen2_frame = tk.Frame(root)

label_screen2 = tk.Label(screen2_frame, text="Claimed Rooms", font=("Helvetica", 18))
label_screen2.pack(pady=10)

back_button2 = tk.Button(screen2_frame, text="Back to Main Menu", command=lambda: back_to_main_menu(screen2_frame))
back_button2.pack(pady=5)

# Table for all rooms
table_frame = tk.Frame(root)
table_frame.pack()

columns = ("ID", "Beds", "Price", "VIP", "Claimed", "Start Date", "End Date", "Claimer Name")

# Table for all rooms
table_tree = ttk.Treeview(table_frame, columns=columns, show="headings")
for col in columns:
    table_tree.heading(col, text=col)
table_tree.pack(side=tk.LEFT, padx=10, pady=10, fill="both", expand=True)
table_tree.bind("<ButtonRelease-1>", on_tree_click)

# Table for non-claimed rooms
table_non_claimed_tree = ttk.Treeview(table_frame, columns=columns, show="headings")
for col in columns:
    table_non_claimed_tree.heading(col, text=col)
table_non_claimed_tree.pack(side=tk.LEFT, padx=10, pady=10, fill="both", expand=True)
table_non_claimed_tree.bind("<ButtonRelease-1>", on_tree_click)

# Table for claimed rooms
table_claimed_tree = ttk.Treeview(table_frame, columns=columns, show="headings")
for col in columns:
    table_claimed_tree.heading(col, text=col)
table_claimed_tree.pack(side=tk.LEFT, padx=10, pady=10, fill="both", expand=True)
table_claimed_tree.bind("<ButtonRelease-1>", on_tree_click)

# Initially show the main menu
open_screen(main_menu_frame)

root.mainloop()
