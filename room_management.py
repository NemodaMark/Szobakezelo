from room_define import room

class management:
    @staticmethod
    def reader():
        all_rooms = []
        path = "assets/datas/rooms.txt"
        with open(path, "r") as reader:
            for line in reader:
                room_data = line.strip().split(";")
                if len(room_data) < 7:
                    default_values = room.default_values()
                    room_data = [default_values[key] if key not in room_data else room_data[room_data.index(key)] for key in default_values.keys()]
                room_object = room(room_data[0], room_data[1], room_data[2], room_data[3], room_data[4], room_data[5], room_data[6], room_data[7])
                all_rooms.append(room_object)
        return all_rooms

    @staticmethod
    def book(all_rooms, user_data):
        room_number, user_name, user_start, user_end = user_data
        for room in all_rooms:
            if int(room.id) == int(room_number):
                if room.claimed == "1":
                    print("This room is already claimed.")
                    return
                room.claimed = "1"
                room.start_date = user_start
                room.end_date = user_end
                room.claimer_name = user_name
                print("The booking was successful.")
                break
        else:
            print("The given room number does not exist.")

        # Write the changes back to the file
        path = "assets/datas/rooms.txt"
        with open(path, "w") as writer:
            for room in all_rooms:
                writer.write(f"{room.id};{room.beds};{room.price};{room.vip};{room.claimed};{room.start_date};{room.end_date};{room.claimer_name}\n")

    @staticmethod
    def cancel(all_rooms, room_number):
        for room in all_rooms:
            if int(room.id) == int(room_number):
                room.claimed = "0"
                room.start_date = ""
                room.end_date = ""
                room.claimer_name = ""
                print("The booking was successfully cancelled.")
                break
        else:
            print("The given room number does not exist.")

        # Write the changes back to the file
        path = "assets/datas/rooms.txt"
        with open(path, "w") as writer:
            for room in all_rooms:
                writer.write(f"{room.id};{room.beds};{room.price};{room.vip};{room.claimed};{room.start_date};{room.end_date};{room.claimer_name}\n")
