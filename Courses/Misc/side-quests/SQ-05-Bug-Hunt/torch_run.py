# torch_run.py
#
# A short dungeon crawl. You start at the entrance with three torches.
# Moving between rooms burns a torch. Find the lantern before you run out
# of torches, then reach the exit.
#
# Commands: north, south, east, west, look, take, inventory, quit

MAX_TORCHES = 3

room = "entrance"
torches = MAX_TORCHES
has_lantern = False
has_key = False
moves_made = 0
playing = True

print("TORCH RUN")
print("=========")
print("You are at the entrance of a cold stone dungeon.")
print("You are carrying 3 torches. Moving burns one.")
print("Type 'look' to see the room, or a direction to move.")
print()

while playing:

    command = input("> ").strip().lower()
    moves_made = moves_made + 1

    # ----- Movement -----
    if command == "north" or command == "south" or command == "east" or command == "west":

        # Burn a torch for the move.
        torches = torches - 1

        if torches < 0:
            print("Your last torch gutters out. The dark takes you.")
            playing = False

        # Work out the new room from the current room and the direction.
        if room == "entrance":
            if command == "north":
                room = "hall"
            elif command == "east":
                room = "storeroom"
            else:
                print("Solid rock that way.")
        elif room == "hall":
            if command == "north":
                room = "vault"
            elif command == "south":
                room = "entrance"
            else:
                print("Solid rock that way.")
        elif room == "storeroom":
            if command == "west":
                room = "entrance"
            else:
                print("Solid rock that way.")
        elif room == "vault":
            if command == "south":
                room = "hall"
            else:
                print("Solid rock that way.")

        print("You are in the " + room + ".")
        print("Torches left: " + str(torches))

    # ----- Looking -----
    elif command == "look":
        if room == "entrance":
            print("A wide arch behind you. Passages north and east.")
        elif room == "storeroom":
            if has_lantern == False:
                print("Shelves of rotted sacks. A brass lantern sits on a crate.")
            else:
                print("Shelves of rotted sacks. The crate is empty.")
        elif room == "hall":
            print("A long hall. Something glints on the floor.")
        elif room == "vault":
            print("A heavy door, locked. This is the way out.")

    # ----- Taking -----
    elif command == "take":
        if room == "storeroom":
            has_lantern = True
            print("You take the brass lantern. It will not burn out.")
        elif room == "hall":
            has_key = True
            print("You pick up an iron key.")
        else:
            print("Nothing here to take.")

    # ----- Inventory -----
    elif command == "inventory":
        print("Torches: " + str(torches))
        if has_lantern:
            print("Brass lantern")
        if has_key:
            print("Iron key")

    elif command == "quit":
        print("You turn back. Nobody blames you.")
        playing = False

    else:
        print("You cannot do that here.")

    # ----- Win check -----
    if room == "vault" and has_key == True:
        print("The iron key turns. You step out into daylight.")
        print("Moves taken: " + str(moves_made))
        playing = False
