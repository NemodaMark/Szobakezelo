import sys
import os

all_rooms = []
claimed_rooms = []
unclaimed_rooms = []


def menu():
    print("0 - Bezárás")
    print("1 - Foglalás")
    print("2 - Lemondás")
    print("3 - Listázás")
    select = int(input("Választás: "))

    if select == 0:
        bezaras()
    elif select == 1:
        foglalas()
    elif select == 2:
        lemondas()
    elif select == 3:
        listazas()
    else:
       return menu()


def bezaras():
   return sys.exit()


def listazas():
    clear_console()
    print("Szobák listája:")
    print("{:<15} {:<10} {:<10} {:<5} {:<15} {:<20}".format(
        "Szoba Szám", "Ágyak", "Ár", "VIP", "Dátum", "Foglaló Neve"))
    print("-" * 80)

    # Sort rooms by room number
    sorted_rooms = sorted(all_rooms, key=lambda x: int(x['room_number']))

    for room in sorted_rooms:
        # Convert VIP status to "Igen" or "Nem"
        vip_status = "Igen" if room['vip'] == '1' else "Nem"
        print("{:<15} {:<10} {:<10} {:<5} {:<15} {:<20}".format(
            room['room_number'], room['beds'], room['price'], vip_status,
            room['date'], room['name_of_claimer']))
    print("-" * 80)
    return menu()


from datetime import datetime


def update_data_file():
    # Open the file in write mode to update the data
    with open('data.txt', 'w') as file:
        # Write the updated data for all rooms
        for room in all_rooms:
            file.write(';'.join(room.values()) + '\n')


from datetime import datetime


def foglalas():
    clear_console()
    print("Szobák listája:")
    print("{:<15} {:<10} {:<10} {:<5} {:<15} {:<20}".format(
        "Szoba Szám", "Ágyak", "Ár", "VIP", "Dátum", "Foglaló Neve"))
    print("-" * 80)

    # Sort rooms by room number
    sorted_rooms = sorted(unclaimed_rooms, key=lambda x: int(x['room_number']))

    for room in sorted_rooms:
        # Convert VIP status to "Igen" or "Nem"
        vip_status = "Igen" if room['vip'] == '1' else "Nem"
        print("{:<15} {:<10} {:<10} {:<5} {:<15} {:<20}".format(
            room['room_number'], room['beds'], room['price'], vip_status,
            room['date'], room['name_of_claimer']))
    print("-" * 80)

    # Foglalás rész
    claiming_room_number = input("Melyik szobát szeretné lefoglalni? Adja meg a szoba számát: ")

    # Check if the claimed room number is valid and unclaimed
    found_room = None
    for room in unclaimed_rooms:
        if room['room_number'] == claiming_room_number:
            found_room = room
            break

    if found_room:
        # Prompt the user to enter the start date of the claim
        claim_start_date_str = input("Adja meg a foglalás kezdő dátumát (ÉÉÉÉ-HH-NN formátumban): ")

        # Parse the start date string into a datetime object
        try:
            claim_start_date = datetime.strptime(claim_start_date_str, '%Y-%m-%d')
        except ValueError:
            print("Érvénytelen dátum formátum. Kérjük, használja az ÉÉÉÉ-HH-NN formátumot.")
            return foglalas()  # Retry if the date format is invalid

        # Update the room information
        found_room['claimed'] = '1'
        found_room['date'] = claim_start_date_str
        claimer_name = input("Kérjük, adja meg a foglaló nevét: ")
        found_room['name_of_claimer'] = claimer_name

        # Write the updated room information to the data.txt file
        with open('data.txt', 'w') as file:
            for room in all_rooms:
                file.write(';'.join(room.values()) + '\n')

        print(f"A(z) {claiming_room_number} szoba sikeresen lefoglalva {claimer_name} név alatt.")

        # Close the file
        file.close()

        # Re-read the file to update room information
        runtime()
    else:
        print("A megadott szobaszám nem érvényes vagy már foglalt.")

    input("Nyomjon Enter-t a főmenübe való visszatéréshez...")
    return menu()


def lemondas():
    clear_console()
    print("Foglalt szobák listája:")
    print("{:<15} {:<10} {:<10} {:<5} {:<15} {:<20}".format(
        "Szoba Szám", "Ágyak", "Ár", "VIP", "Dátum", "Foglaló Neve"))
    print("-" * 80)

    # Sort rooms by room number
    sorted_rooms = sorted(claimed_rooms, key=lambda x: int(x['room_number']))

    for room in sorted_rooms:
        # Convert VIP status to "Igen" or "Nem"
        vip_status = "Igen" if room['vip'] == '1' else "Nem"
        print("{:<15} {:<10} {:<10} {:<5} {:<15} {:<20}".format(
            room['room_number'], room['beds'], room['price'], vip_status,
            room['date'], room['name_of_claimer']))
    print("-" * 80)

    # Lemondás rész
    canceling_room_number = input("Melyik szobát szeretné lemondani? Adja meg a szoba számát: ")

    # Check if the canceled room number is valid and claimed
    found_room = None
    for room in claimed_rooms:
        if room['room_number'] == canceling_room_number:
            found_room = room
            break

    if found_room:
        # Update the room information
        found_room['claimed'] = '0'
        found_room['date'] = ''
        found_room['name_of_claimer'] = ''

        # Write the updated room information to the data.txt file
        with open('data.txt', 'w') as file:
            for room in all_rooms:
                file.write(';'.join(room.values()) + '\n')

        print(f"A(z) {canceling_room_number} szoba foglalása sikeresen lemondva.")
    else:
        print("A megadott szobaszám nem érvényes vagy nincs foglalva.")

    input("Nyomjon Enter-t a főmenübe való visszatéréshez...")

    # Reinitialize the lists after updating the data file
    return runtime()



def runtime():
    # Clear existing room lists to avoid duplicates
    all_rooms.clear()
    claimed_rooms.clear()
    unclaimed_rooms.clear()

    # Open the file in read mode
    with open('data.txt', 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

        # Process each line
        for line in lines:
            # Split the line into fields based on the semicolon delimiter
            fields = line.strip().split(';')

            # Create a dictionary to represent the room
            room_info = {
                'room_number': fields[0],
                'beds': fields[1],
                'price': fields[2],
                'vip': fields[3],
                'claimed': fields[4],
                'date': fields[5],
                'name_of_claimer': fields[6]
            }

            # Add the room to the all_rooms list
            all_rooms.append(room_info)

            # Check if the room is claimed or unclaimed
            if room_info['claimed'] == '1':
                claimed_rooms.append(room_info)
            else:
                unclaimed_rooms.append(room_info)

    # Return all three lists/dictionaries
    return all_rooms, claimed_rooms, unclaimed_rooms, menu()


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



runtime()