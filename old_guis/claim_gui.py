import tkinter as tk
from room_management import manage
import claim_data_gui

class RoomTable:
    def __init__(self, root):
        self.root = root
        self.rooms = [room for room in manage.read() if room.claimed == "0"]

        print("Number of rooms:", len(self.rooms))  # Debugging: Print number of rooms
        print("Rooms:", self.rooms)  # Debugging: Print contents of rooms list

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
            frame = tk.Frame(self.table_body, bg="#f0f0f0" if i % 2 == 0 else "#e0e0e0")
            frame.pack(fill=tk.X)
            labels = [room.id, room.beds, room.price, room.vip, room.claimed, room.start_date, room.end_date, room.claimer_name]
            for j, label in enumerate(labels):
                tk.Label(frame, text=str(label), font=("Arial", 12), bg=frame.cget("bg"), relief="flat").grid(row=0, column=j, padx=5, pady=5, sticky="w")
            # Add button to open claim data GUI
            button = tk.Button(frame, text="Foglalás", font=("Arial", 12), command=lambda room_id=room.id: self.open_claim_data(room_id))
            button.grid(row=0, column=8, padx=5, pady=5)

    def open_claim_data(self, room_id):
        # Open claim data GUI and pass room ID
        claim_data_gui.open_claim_gui(room_id)

root = tk.Tk()

# Create table
table = RoomTable(root)

root.mainloop()
