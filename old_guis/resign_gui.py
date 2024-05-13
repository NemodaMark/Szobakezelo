import tkinter as tk
from room_management import manage

class RoomTable:
    def __init__(self, root):
        self.root = root
        self.rooms = [room for room in manage.read() if room.claimed == "1"]  # Only claimed rooms
        print("Number of rooms:", len(self.rooms))  # Debugging: Print number of rooms

        # Create table header
        header = tk.Frame(self.root, bg="#f0f0f0")
        header.pack(pady=10, fill=tk.X)

        labels = ["ID", "Beds", "Price", "VIP", "Claimed", "Start Date", "End Date", "Claimer Name", "Button"]
        for i, label in enumerate(labels):
            tk.Label(header, text=label, font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row=0, column=i, padx=5, pady=5)

        # Create table body
        self.table_body = tk.Frame(self.root)
        self.table_body.pack(fill=tk.BOTH, expand=True)

        self.create_table_rows()

    def create_table_rows(self):
        for i, room in enumerate(self.rooms):
            print("Room", room.id, "claimed:", room.claimed)  # Debugging: Print room's claimed status
            frame = tk.Frame(self.table_body, bg="#f0f0f0" if i % 2 == 0 else "#e0e0e0")
            frame.pack(fill=tk.X)

            # Create labels for room data
            labels = [room.id, room.beds, room.price, room.vip, room.claimed, room.start_date, room.end_date, room.claimer_name]
            for j, label in enumerate(labels):
                tk.Label(frame, text=str(label), font=("Arial", 12), bg=frame.cget("bg"), relief="flat").grid(row=i, column=j, padx=5, pady=5, sticky="w")
            
            # Create button for resigning
            button = tk.Button(frame, text="Lemondás", font=("Arial", 12), command=lambda room_id=room.id: manage.resign(room_id))
            button.grid(row=i, column=8, padx=5, pady=5)

    def update_table(self):
        # Clear the existing table
        for widget in self.table_body.winfo_children():
            widget.destroy()
        
        # Reload the room data and recreate the table
        self.rooms = [room for room in manage.read() if room.claimed == "1"]  # Filter claimed rooms again
        print("Number of rooms after update:", len(self.rooms))  # Debugging: Print updated number of rooms
        self.create_table_rows()

root = tk.Tk()

# Create table
table = RoomTable(root)

root.mainloop()
