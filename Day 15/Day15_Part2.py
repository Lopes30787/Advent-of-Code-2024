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
            if char == "O":
                row += "["
                row += "]"
            
            elif char == "#":
                row += char
                row += char

            else:
                row += char
                row += "."
        
        if char == "@":
            current = [i,j]
        
        j += 2


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

        elif up == "[" or up == "]":
            stack = [[current[0]-1,current[1]],]
            change = []
            nothing_below = []
            valid = True

            if up == "[":
                stack += [[current[0]-1,current[1]+1],]
            else:
                stack += [[current[0]-1,current[1]-1],]

            while stack != []:
                checking = stack.pop(0)
                change += [checking,]

                if warehouse[checking[0]-1][checking[1]] == "[":
                    if [checking[0]-1,checking[1]] not in stack:
                        stack += [[checking[0]-1,checking[1]],]
                        stack += [[checking[0]-1,checking[1]+1],]

                elif warehouse[checking[0]-1][checking[1]] == "]":
                    if [checking[0]-1,checking[1]] not in stack:
                        stack += [[checking[0]-1,checking[1]],]
                        stack += [[checking[0]-1,checking[1]-1],]

                elif warehouse[checking[0]-1][checking[1]] == "#":
                    valid = False
                    break

                if [checking[0]+1,checking[1]] not in change:
                    nothing_below += [checking,]
            
            if valid:
                for box in reversed(change):
                    warehouse[box[0]-1][box[1]] = warehouse[box[0]][box[1]]

                    if box in nothing_below:
                        warehouse[box[0]][box[1]] = "."

                warehouse[current[0]-1][current[1]] = "@"
                warehouse[current[0]][current[1]] = "."
                current[0] -= 1

            

    if direction == "v":
        down = warehouse[current[0]+1][current[1]]

        if down == ".":
            warehouse[current[0]][current[1]] = "."
            warehouse[current[0]+1][current[1]] = "@"
            current[0] += 1

        elif down == "[" or down == "]":
            stack = [[current[0]+1,current[1]],]
            change = []
            nothing_up = []
            valid = True

            if down == "[":
                stack += [[current[0]+1,current[1]+1],]
            else:
                stack += [[current[0]+1,current[1]-1],]

            while stack != []:

                checking = stack.pop(0)
                change += [checking,]

                if warehouse[checking[0]+1][checking[1]] == "[":
                    if [checking[0]+1,checking[1]] not in stack:
                        stack += [[checking[0]+1,checking[1]],]
                        stack += [[checking[0]+1,checking[1]+1],]

                elif warehouse[checking[0]+1][checking[1]] == "]":
                    if [checking[0]+1,checking[1]] not in stack:
                        stack += [[checking[0]+1,checking[1]],]
                        stack += [[checking[0]+1,checking[1]-1],]

                elif warehouse[checking[0]+1][checking[1]] == "#":
                    valid = False
                    break

                if [checking[0]-1,checking[1]] not in change:
                    nothing_up += [checking,]

            if valid:
                for box in reversed(change):
                    warehouse[box[0]+1][box[1]] = warehouse[box[0]][box[1]]

                    if box in nothing_up:
                        warehouse[box[0]][box[1]] = "."

                warehouse[current[0]+1][current[1]] = "@"
                warehouse[current[0]][current[1]] = "."
                current[0] += 1
    
    if direction == ">":
        right = warehouse[current[0]][current[1]+1]

        if right == ".":
            warehouse[current[0]][current[1]] = "."
            warehouse[current[0]][current[1]+1] = "@"
            current[1] += 1

        elif right == "[":
            last = current[1]+1
            while warehouse[current[0]][last+1] == "[" or warehouse[current[0]][last+1] == "]":
                last += 1
            
            if warehouse[current[0]][last+1] != "#":
                warehouse[current[0]][current[1]] = "."
                warehouse[current[0]][current[1]+1] = "@"
                warehouse[current[0]][last+1] = "]"
                current[1] += 1

                for i in range(current[1] + 1, last + 1):
                    if warehouse[current[0]][i] == "[":
                        warehouse[current[0]][i] = "]"

                    elif warehouse[current[0]][i] == "]":
                        warehouse[current[0]][i] = "["

    if direction == "<":
        left = warehouse[current[0]][current[1]-1]

        if left == ".":
            warehouse[current[0]][current[1]] = "."
            warehouse[current[0]][current[1]-1] = "@"
            current[1] -= 1

        elif left == "]":
            last = current[1]-1
            while warehouse[current[0]][last-1] == "[" or warehouse[current[0]][last-1] == "]":
                last -= 1

            if warehouse[current[0]][last-1] != "#":
                warehouse[current[0]][current[1]] = "."
                warehouse[current[0]][current[1]-1] = "@"
                warehouse[current[0]][last-1] = "["      
                current[1] -= 1          
           

                for i in range(current[1] - 1, last - 1, -1):
                    if warehouse[current[0]][i] == "[":
                        warehouse[current[0]][i] = "]"

                    elif warehouse[current[0]][i] == "]":
                        warehouse[current[0]][i] = "["
            
def calculate_gps():
    gps = 0

    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == "[":
                gps += (100*i + j)

    return gps

for line in file:
    for direction in line:
        check_movement(direction)

print(calculate_gps())