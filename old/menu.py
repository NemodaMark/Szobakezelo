import roomManager
from room import Room
import sys, os
from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'

class Menu:
    def __init__(self, room_manager: roomManager.RoomManager):
        self.room_manager = room_manager

    def display_menu(self) -> None:
        print("0 - Bezárás")
        print("1 - Foglalás")
        print("2 - Lemondás")
        print("3 - Listázás")
        select = int(input("Választás: "))
        if select == 0:
            self.bezaras()
        elif select == 1:
            self.foglalas()
        elif select == 2:
            self.lemondas()
        elif select == 3:
            self.listazas()
        else:
            print("Érvénytelen választás. Kérjük, próbálja újra.")
            self.display_menu()

    def bezaras(self) -> None:
        sys.exit()

    def display_room_list(self, rooms: list[Room]) -> list[Room]:
        clear_console()
        print("Szobák listája:")
        print("{:<15} {:<10} {:<10} {:<5} {:<15} {:<20}".format(
            "Szoba Szám", "Ágyak", "Ár", "VIP", "Dátum", "Foglaló Neve"))
        print("-" * 80)

        sorted_rooms = sorted(rooms, key=lambda x: int(x.room_number))

        for room in sorted_rooms:
            vip_status = "✓" if room.vip == '1' else "ⓧ"
            print("{:<15} {:<10} {:<10} {:<5} {:<15} {:<20}".format(
                room.room_number, room.beds, room.price, vip_status,
                room.date.strftime(DATE_FORMAT) if room.date else '', room.claimer_name))
        print("-" * 80)

        return sorted_rooms

    def foglalas(self) -> None:
        self.display_room_list(self.room_manager.unclaimed_rooms)
        claiming_room_number = input("Melyik szobát szeretné lefoglalni? Adja meg a szoba számát: ")
        found_room = self.find_room(claiming_room_number, self.room_manager.unclaimed_rooms)
        if found_room:
            claim_start_date_str = input(f"Adja meg a foglalás kezdő dátumát ({DATE_FORMAT} formátumban): ")
            try:
                claim_start_date = datetime.strptime(claim_start_date_str, DATE_FORMAT)
            except ValueError:
                raise ValueError("Érvénytelen dátum formátum. Kérjük, használja az ÉÉÉÉ-HH-NN formátumot.")

            found_room.update_booking_info('1', claim_start_date_str, input("Kérjük, adja meg a foglaló nevét: "))

            self.room_manager.update_data_file()
            self.room_manager.load_data_from_file()
            print(f"A(z) {claiming_room_number} szoba sikeresen lefoglalva.")
        else:
            print("A megadott szobaszám nem érvényes vagy már foglalt.")

        input("Nyomjon Enter-t a főmenübe való visszatéréshez...")
        self.display_menu()

    def lemondas(self) -> None:
        self.display_room_list(self.room_manager.claimed_rooms)
        canceling_room_number = input("Melyik szobát szeretné lemondani? Adja meg a szoba számát: ")
        found_room = self.find_room(canceling_room_number, self.room_manager.claimed_rooms)
        if found_room:
            found_room.update_booking_info('0', '', '')

            self.room_manager.update_data_file()
            self.room_manager.load_data_from_file()
            print(f"A(z) {canceling_room_number} szoba foglalása sikeresen lemondva.")
        else:
            print("A megadott szobaszám nem érvényes vagy nincs foglalva.")

        input("Nyomjon Enter-t a főmenübe való visszatérésheul...")
        self.display_menu()

    def find_room(self, room_number: str, rooms: list[roomManager.Room]) -> roomManager.Room:
        for room in rooms:
           if room.room_number == room_number:
                return room
        return None

    def listazas(self) -> None:
        self.display_room_list(self.room_manager.all_rooms)
        input("Nyomjon Enter-t a főmenübe való visszatéréshez...")
        self.display_menu()

def clear_console() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def main() -> None:
    room_manager = roomManager.RoomManager()
    room_manager.load_data_from_file()
    menu = Menu(room_manager)
    menu.display_menu()

if __name__ == "__main__":
    main()