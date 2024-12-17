file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 15\\Day15.txt', 'r')

warehouse = []
current = []

i = 0
for line in file:
    if line == "\n":
        break
    
    row = []
    
    j = 0
    for char in line:
        if char != "\n":
            row += char
        
        if char == "@":
            current = [i,j]
        
        j += 1


    warehouse += [row,]
    i += 1

def check_movement(direction):

    global warehouse
    global current

    if direction == "^":
        up = warehouse[current[0]-1][current[1]]

        if up == ".":
            warehouse[current[0]][current[1]] = "."
            warehouse[current[0]-1][current[1]] = "@"
            current[0] -= 1

        elif up == "O":
            last = current[0]-1
            while warehouse[last-1][current[1]] == "O":
                last -= 1
            
            if warehouse[last-1][current[1]] != "#":
                warehouse[current[0]][current[1]] = "."
                warehouse[current[0]-1][current[1]] = "@"
                warehouse[last-1][current[1]] = "O"
                current[0] -= 1

    if direction == "v":
        down = warehouse[current[0]+1][current[1]]

        if down == ".":
            warehouse[current[0]][current[1]] = "."
            warehouse[current[0]+1][current[1]] = "@"
            current[0] += 1

        elif down == "O":
            last = current[0]+1
            while warehouse[last+1][current[1]] == "O":
                last += 1
            
            if warehouse[last+1][current[1]] != "#":
                warehouse[current[0]][current[1]] = "."
                warehouse[current[0]+1][current[1]] = "@"
                warehouse[last+1][current[1]] = "O"
                current[0] += 1
    
    if direction == ">":
        right = warehouse[current[0]][current[1]+1]

        if right == ".":
            warehouse[current[0]][current[1]] = "."
            warehouse[current[0]][current[1]+1] = "@"
            current[1] += 1

        elif right == "O":
            last = current[1]+1
            while warehouse[current[0]][last+1] == "O":
                last += 1
            
            if warehouse[current[0]][last+1] != "#":
                warehouse[current[0]][current[1]] = "."
                warehouse[current[0]][current[1]+1] = "@"
                warehouse[current[0]][last+1] = "O"
                current[1] += 1

    if direction == "<":
        left = warehouse[current[0]][current[1]-1]

        if left == ".":
            warehouse[current[0]][current[1]] = "."
            warehouse[current[0]][current[1]-1] = "@"
            current[1] -= 1

        elif left == "O":
            last = current[1]-1
            while warehouse[current[0]][last-1] == "O":
                last -= 1
            
            if warehouse[current[0]][last-1] != "#":
                warehouse[current[0]][current[1]] = "."
                warehouse[current[0]][current[1]-1] = "@"
                warehouse[current[0]][last-1] = "O"
                current[1] -= 1
            
def calculate_gps():
    gps = 0

    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == "O":
                gps += (100*i + j)

    return gps


for line in file:
    for direction in line:
        check_movement(direction)

print(calculate_gps())