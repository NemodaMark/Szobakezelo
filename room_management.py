import room_define

class manage:
    
    def read():
        rooms = []
        reader = open("assets\important_datas\data.txt", "r")
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
            
    # def write():
    #     #writing

    # def delete():

    #     #deleting

    # def update():

    #     #updating
    
    # def save_data():
    #     #saving data

    # def load_data():

    #     #loading data
    read()