import update
import game_map
import sys
health = 100
max_health = 100
hunger = 100
global x, y
x = 1
y = 1
xp = 2
game_map.init_map()
def game_loop():
    global x, y
    while True:
        update.update(health, max_health, hunger, 2, x, y, xp, required_levels)
        io = input("Where do you want to go? >")
        if io == "w":
            if game_map.find_neighbour(x, y, "up", 0) == 0:
                print("Can't go there.")
            else:
                y = y - 1
        if io == "s":
            if game_map.find_neighbour(x, y, "down", 0) == 0:
                print("Can't go there.")
            else:
                y = y + 1
        if io == "a":
            if game_map.find_neighbour(x, y, "left", 0) == 0:
                print("Can't go there.")
            else:
                x = x - 1
        if io == "d":
            if game_map.find_neighbour(x, y, "right", 0) == 0:
                print("Can't go there.")
            else:
                x = x + 1
# The code for finding what level the player is is at update.py
required_levels = [-1, 0, 100]
for i in range(100):
    required_levels.append(required_levels[-1] * 1.5)
try:
    print(r"=============================================================""")
    print(r"""=   ____                  _     _____                       =""")
    print(r"""=  / __ \                | |   |  __ \                      =""")
    print(r"""= | |  | |_   _  ___  ___| |_  | |  | | ___ _ __ ___   ___  =""")
    print(r"""= | |  | | | | |/ _ \/ __| __| | |  | |/ _ \ '_ ` _ \ / _ \ =""")
    print(r"""= | |__| | |_| |  __/\__ \ |_  | |__| |  __/ | | | | | (_)| =""")
    print(r"""= \___\_\\__,_|\___||___/\__| |_____/ \___|_| |_| |_|\___/  =""")
    print(r"""=============================================================""")
except SyntaxWarning as s:
    pass
print("Welcome to the QuestDemo! What would you like to do?")
print("[P]lay!")
print("\n")
print("[M]anual!")
print("\n")
print("[S]ettings!")
print("\n")
print("E[X]it!")
start_input = input("> ")
if start_input.lower() == "p" or start_input.lower() == "play":
    game_loop()
elif start_input.lower() == "m" or start_input.lower() == "manual":
    try:
        print(r"""=====================================""")
        print(r"""=  __  __                         _ =""")
        print(r"""= |  \/  |                       | |=""")
        print(r"""= | \  / | __ _ _ __  _   _  __ _| |=""")
        print(r"""= | |\/| |/ _` | '_ \| | | |/ _` | |=""")
        print(r"""= | |  | | (_| | | | | |_| | (_| | |=""")
        print(r"""= |_|  |_|\__,_|_| |_|\__,_|\__,_|_|=""")
        print(r"""=====================================""")
    except SyntaxWarning as s:
        pass
    print("Press w, a, s or d to move around the game.")
    print("Currently, most things are unused. Just walk about I guess.")
    print("Ready to play?")
    print("[Y]es!")
    print("[N]o!")
    man_input = input("> ")
    if man_input.lower() == "y" or man_input.lower() == "yes":
        game_loop()
    else:
        sys.exit()
elif start_input.lower() == "settings" or start_input.lower() == "s":
    print()
else:
    sys.exit()