import os
from datetime import datetime
from room import Room

class RoomManager:
    def __init__(self):
        self.all_rooms = []
        self.unclaimed_rooms = []
        self.claimed_rooms = []
        self.file_path = "assets/importatnDatas/data.txt"

    def load_data_from_file(self):
        if not os.path.exists(self.file_path):
            return
        with open(self.file_path, "r") as file:
            for line in file:
                data = line.strip().split(";")
                room_number, beds, price, vip, date_str, claimer_name = data
                date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
                room = Room(room_number, int(beds), price, vip, date, claimer_name)
                self.add_room(room)

    def save_data_to_file(self, file):
        for room in self.all_rooms:
            file.write(f"{room.room_number};{room.beds};{room.price};{room.vip};{room.date.strftime('%Y-%m-%d %H:%M:%S')};{room.claimer_name}\n")

    def add_room(self, room: Room):
        self.all_rooms.append(room)
        if room.claimer_name is None:
            self.unclaimed_rooms.append(room)
        else:
            self.claimed_rooms.append(room)

    def create_room(self, room_number: str, beds: int, price: str, vip: str, date: datetime, claimer_name: str):
        room = Room(room_number, beds, price, vip, date, claimer_name)
        self.add_room(room)

    def delete_room(self, room: Room):
        self.all_rooms.remove(room)
        if room.claimer_name is None:
            self.unclaimed_rooms.remove(room)
        else:
            self.claimed_rooms.remove(room)

    def check_room_exists(self, room_number):
        for room in self.all_rooms:
            if room.room_number == room_number:
                return True
        return False

    def claim_room(self, room_number, claimer_name):
        for room in self.unclaimed_rooms:
            if room.room_number == room_number:
                room.claimer_name = claimer_name
                self.claimed_rooms.append(room)
                self.unclaimed_rooms.remove(room)

    def unclaim_room(self, room_number):
        for room in self.claimed_rooms:
            if room.room_number == room_number:
                room.claimer_name = None
                self.unclaimed_rooms.append(room)
                self.claimed_rooms.remove(room)

    def get_claimer_name(self, room_number):
        for room in self.claimed_rooms:
            if room.room_number == room_number:
                return room.claimer_name
        return None

    def get_room_by_number(self, room_number):
        for room in self.all_rooms:
            if room.room_number == room_number:
                return room
        return None