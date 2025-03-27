import game_map
import tools
global level, xq_required
def update(health, max_health, hunger, saturation, x, y, xp, required_levels):
    tools.clear_screen()
    print(f'Health: {health}/{max_health}')
    print(f'Hunger: {hunger}')
    print("\n")
    print(f'You are at X:{x} Y:{y}')
    print(f'In front of you is {game_map.find_neighbour(x, y, "up", 1)}')
    print(f'To the left of you is {game_map.find_neighbour(x, y, "left", 1)}')
    print(f'To the right of you is {game_map.find_neighbour(x, y, "right", 1)}')
    print(f'Behind you is {game_map.find_neighbour(x, y, "down", 1)}')
    print(f'You are standing on {game_map.find_neighbour(x, y, "current", 1)}')
    print("\n")
    for i in range(len(required_levels)):
        if required_levels[i] > xp:
            if i - 1 == 101:
                level = 1
            else:
                level = i - 1
            xp_required = required_levels[i] - xp
            break
    hunger = hunger - saturation
    print(f'Level: {level}')
    print(f'XP required for next level: {xp_required}')
    print("\n")

