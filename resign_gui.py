import tkinter as tk
from room_management import manage

class RoomTable:
    def __init__(self, root):
        self.root = root
        self.rooms = manage.read()

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
            if room.claimed != 0:
                frame = tk.Frame(self.table_body, bg="#f0f0f0" if i % 2 == 0 else "#e0e0e0")
                frame.pack(fill=tk.X)
                labels = [room.id, room.beds, room.price, room.vip, room.claimed, room.start_date, room.end_date, room.claimer_name]
                for j, label in enumerate(labels):
                    tk.Label(frame, text=str(label), font=("Arial", 12), bg=frame.cget("bg"), relief="flat").grid(row=0, column=j, padx=5, pady=5, sticky="w")
                button = tk.Button(frame, text="Lemondás", font=("Arial", 12))
                button.grid(row=0, column=8, padx=5, pady=5)

root = tk.Tk()

# Create table
table = RoomTable(root)

root.mainloop()