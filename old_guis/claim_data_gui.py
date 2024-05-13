import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from datetime import datetime
import room_management

class Application(tk.Tk):
    def __init__(self, room_id):
        tk.Tk.__init__(self)
        self.room_id = room_id  # Store the room ID

        self.title("Tkinter GUI")

        # create label and entry box for name
        tk.Label(self, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)

        # create dropdowns for start date
        tk.Label(self, text="Start:").grid(row=1, column=0)
        self.start_year = ttk.Combobox(self, state="readonly")
        self.start_year['values'] = [str(y) for y in range(datetime.now().year, datetime.now().year+11)]
        self.start_year.current(0)
        self.start_year.grid(row=1, column=1)

        self.start_month = ttk.Combobox(self, state="readonly")
        self.start_month['values'] = [str(m) for m in range(1, 13)]
        self.start_month.current(0)
        self.start_month.grid(row=1, column=2)

        self.start_day = ttk.Combobox(self, state="readonly")
        self.start_day['values'] = [str(d) for d in range(1, 32)]
        self.start_day.current(0)
        self.start_day.grid(row=1, column=3)

        # create dropdowns for end date
        tk.Label(self, text="End:").grid(row=2, column=0)
        self.end_year = ttk.Combobox(self, state="readonly")
        self.end_year['values'] = [str(y) for y in range(datetime.now().year, datetime.now().year+11)]
        self.end_year.current(0)
        self.end_year.grid(row=2, column=1)

        self.end_month = ttk.Combobox(self, state="readonly")
        self.end_month['values'] = [str(m) for m in range(1, 13)]
        self.end_month.current(0)
        self.end_month.grid(row=2, column=2)

        self.end_day = ttk.Combobox(self, state="readonly")
        self.end_day['values'] = [str(d) for d in range(1, 32)]
        self.end_day.current(0)
        self.end_day.grid(row=2, column=3)

        # create button
        tk.Button(self, text="Send", command=self.send_data).grid(row=3, column=1)

    def send_data(self):
        # get data from entry and dropdowns
        name = self.name_entry.get()
        start_year = self.start_year.get()
        start_month = self.start_month.get()
        start_day = self.start_day.get()
        end_year = self.end_year.get()
        end_month = self.end_month.get()
        end_day = self.end_day.get()

        # check if name is not empty and does not contain special characters
        if not name or any(c in "!,:?" for c in name):
            messagebox.showerror("Error", "Name cannot be empty or contain special characters")
            return

        # check if start date is not in the past or today
        start_date = datetime(int(start_year), int(start_month), int(start_day))
        if start_date <= datetime.now():
            messagebox.showerror("Error", "Start date cannot be in the past or today")
            return

        # check if end date is not in the past or today
        end_date = datetime(int(end_year), int(end_month), int(end_day))
        if end_date <= datetime.now():
            messagebox.showerror("Error", "End date cannot be in the past or today")
            return

        # if all checks pass, save data in a list
        data = [self.room_id, name, start_date, end_date]  # Include room ID in the data
        room_management.manage.write(data)
        print("Data sent successfully:", data)

def open_claim_gui(room_id):
    app = Application(room_id)
    app.mainloop()
