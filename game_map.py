# Game map maker
# y is first, then x
# 0 = Wall/Barrier
# 1 = ground
global grid
grid = []
def init_map():
    # default initialisation, makes everything in a 100x100 grid ground
    for i in range(100):
        grid.append([])
        for e in range(100):
            grid[i].append(1)
    # building the cage
    for i in range (10):
        grid[0][i] = 0
    for i in range(10):
        grid[i][0] = 0
    for i in range(10):
        grid[10][i] = 0
    for i in range(10):
        grid[i][10] = 0

def format_material(material):
    if material == 0:
        return "wall"
    if material == 1:
        return "ground"

def find_neighbour(x, y, direction, formatted):
    if direction == "up":
        if formatted == 1:
            return format_material(grid[y - 1][x])
        else:
            return grid[y - 1][x]
    if direction == "down":
        if formatted == 1:
            return format_material(grid[y + 1][x])
        else:
            return grid[y + 1][x]
    if direction == "left":
        if formatted == 1:
            return format_material(grid[y][x - 1])
        else:
            return grid[y][x - 1]
    if direction == "right":
        if formatted == 1:
            return format_material(grid[y][x + 1])
        else:
            return grid[y][x + 1]
    if direction == "current":
        if formatted == 1:
            return format_material(grid[y][x])
        else:
            return grid[y][x]