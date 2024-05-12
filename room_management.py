import room_define


class manage:

    def read():
        rooms = []
        reader = open("assets/important_datas/data.txt", "r")
        for item in reader:
            i = item.strip().split(";")
            if len(i) < len(room_define.room.default_values()):
                i += [None] * (len(room_define.room.default_values()) - len(i))
            default = room_define.room.default_values()
            my_data = {key: i[index] if i[index] else value for index, (key, value) in enumerate(default.items())}
            room = room_define.room(**my_data)
            rooms.append(room)
        for item in rooms:
            print(item.price)
        return rooms

    def write():
        with open("assets/important_datas/data.txt", "w") as writer:
            for room in rooms:
                # Implement the logic to write the room data to the file
                pass
    def delete():
        room.claimed = 0
        room.start_date = ""
        room.end_date = ""
        room.claimer_name = ""
        # I want to edit room.claimed = 0, start date = " ", end date = " " , claimer name = " "

    read()