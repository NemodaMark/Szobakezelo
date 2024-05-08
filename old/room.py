from datetime import date

class Room:
    def __init__(self, room_number: str, beds: int, price: str, vip: str, date: date, claimer_name: str):
        self.room_number = room_number
        self.beds = beds
        self.price = price
        self.vip = vip
        self.date = date
        self.claimer_name = claimer_name