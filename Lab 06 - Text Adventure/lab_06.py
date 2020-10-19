"""
I apologize in advance for my English.
"""
class Room:
    """
    A room for a text adventure game...
    """
    def __init__(self, description: str, north: int, east: int, south: int, west: int):
        self.description: str = description
        self.north: int = north
        self.east: int  = east
        self.south: int = south
        self.west: int  = west

def get_room_list():
    """
    Returns the initial room_list
    """
    room_list = []
    # 0
    room  = Room(
        "Patio. You are in a patio, it is surrounded by four long walls.\n\
        The south wall has a metal door.",
        north = None,
        east = None,
        south = 2,
        west = None
    )
    room_list.append(room)
    # 1
    room  = Room(
        "Bedroom. You are in a bedroom, there is nothing uncommon.\n\
        The door lead to east",
        north = None,
        east = 2,
        south = None,
        west = None
    )
    room_list.append(room)
    # 2
    room  = Room(
        "Kitchen. You are in a kitchen, there is some porridge on the oven.\n\
        There are three doors, north, west, south",
        north = 0,
        east = None,
        south = 4,
        west = 1
    )
    room_list.append(room)
    # 3
    room  = Room(
        "Tv room. You are in the tv room, there is an old tv set, \n\
        seems like it hasn't being used for years.\n\
        The door lead to east",
        north = None,
        east = 4,
        south = None,
        west = None
    )
    room_list.append(room)
    # 4
    room  = Room(
        "Dinning room. You are in a dinning room, there is a big round table.\n\
        There are three doors, north, west, south",
        north = 2,
        east = None,
        south = 6,
        west = 3
    )
    room_list.append(room)
    # 5
    room  = Room(
        "Master bedroom. You are in the master bedroom, there are many religious things all over.\n\
        The door lead to east",
        north = None,
        east = 6,
        south = None,
        west = None
    )
    room_list.append(room)
    # 6
    room  = Room(
        "Living room. You are in the living room, you can see the exit door to the south.\n\
        There are three doors, north, west, south",
        north = 4,
        east = None,
        south = 7,
        west = 5
    )
    room_list.append(room)
    return room_list

def main():
    #Initialize variables
    done = False
    next_room = 0
    current_room = 0
    room_list = get_room_list()
    # main loop
    print("You can quit any time by typing 'q' or 'quit'.")

    while not done:
        print()
        print(room_list[current_room].description)

        user_input = input("What direction? ").lower()
        #process user input
        if user_input == 'n' or user_input == 'north' :
            next_room = room_list[current_room].north
        elif user_input == 'e' or user_input == 'east' :
            next_room = room_list[current_room].east
        elif user_input == 's' or user_input == 'south' :
            next_room = room_list[current_room].south
        elif user_input == 'w' or user_input == 'west' :
            next_room = room_list[current_room].west
        elif user_input == 'q' or user_input == 'quit' :
            print("Quitting...")
            done = True
            continue
        else:
            # Incorrect input
            print("Can't understand, where would you like to go?")
            continue

        # Check the next room
        if next_room == None:
            print("You can’t go that way")
            print()
        else:
            current_room = next_room
            if next_room == 7:
                print("You won you exited my house...")
                done = True


main()
