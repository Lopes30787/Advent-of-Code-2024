from copy import deepcopy

file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 6\\Day6.txt', 'r')

result = 0
array = []

current_square = []

i = 0
for line in file:
    line_array = []
    j = 0

    for char in line:
        if char == "#":
            line_array += [[char,[], False],]
        elif char == "^":
            line_array += [[".",["up",], False],]
            current_square = [i,j,"up"]
        elif char == ">":
            line_array += [[".",["right"], False],]
            current_square = [i,j,"right"]
        elif char == "v":
            line_array += [[".",["down"], False],]
            current_square = [i,j,"down"]
        elif char == "<":
            line_array += [[".",["left"], False],]
            current_square = [i,j,"left"]
        elif char != "\n":
            line_array += [[".",[], False],]
        j += 1
    
    i += 1
    array += [line_array,]

initial_array = deepcopy(array)
initial_square = current_square.copy()

def check_loop(square, obstacle):
    new_map = deepcopy(initial_array)
    
    square = initial_square.copy()
    new_map[square[0]][square[1]][1] += [square[2],]
    
    while True:
        if square[2] == "up":
            if square[0]-1 >= 0:
                if new_map[square[0]-1][square[1]][0] == "#" or (square[0]-1 == obstacle[0] and square[1] == obstacle[1]):
                    square[2] = "right"
                else:
                    square[0] -= 1

                if square[2] not in new_map[square[0]][square[1]][1]:
                    new_map[square[0]][square[1]][1] += [square[2],]
                else:
                    array[obstacle[0]][obstacle[1]][2] = True
                    return 1
            else:
                break
        
        elif square[2] == "right":
            if square[1]+1 < len(new_map[square[0]]):
                if new_map[square[0]][square[1]+1][0] == "#" or (square[0] == obstacle[0] and square[1]+1 == obstacle[1]):
                    square[2] = "down"
                else:
                    square[1] += 1

                if square[2] not in new_map[square[0]][square[1]][1]:
                    new_map[square[0]][square[1]][1] += [square[2],]
                else:
                    array[obstacle[0]][obstacle[1]][2] = True
                    return 1
            else:
                break
        
        elif square[2] == "down":
            if square[0]+1 < len(new_map):
                if new_map[square[0]+1][square[1]][0] == "#" or (square[0]+1 == obstacle[0] and square[1] == obstacle[1]):
                    square[2] = "left"
                else:
                    square[0] += 1

                if square[2] not in new_map[square[0]][square[1]][1]:
                    new_map[square[0]][square[1]][1] += [square[2],]
                else:
                    array[obstacle[0]][obstacle[1]][2] = True
                    return 1
            else:
                break
        
        elif square[2] == "left":
            if square[1]-1 >= 0:
                if new_map[square[0]][square[1]-1][0] == "#" or (square[0] == obstacle[0] and square[1]-1 == obstacle[1]):
                    square[2] = "up"
                else:
                    square[1] -= 1

                if square[2] not in new_map[square[0]][square[1]][1]:
                    new_map[square[0]][square[1]][1] += [square[2],]
                else:
                    array[obstacle[0]][obstacle[1]][2] = True
                    return 1
            else:
                break
    return 0

while True:

    if current_square[2] == "up":
        if current_square[0]-1 >= 0:
            if array[current_square[0]-1][current_square[1]][0] == "#":
                current_square[2] = "right"
            else:
                if not array[current_square[0]-1][current_square[1]][2]:
                    result += check_loop(current_square,[current_square[0]-1, current_square[1]])
                current_square[0] -= 1

            if current_square[2] not in array[current_square[0]][current_square[1]][1]:
                array[current_square[0]][current_square[1]][1] += [current_square[2],]
        else:
            break
    
    elif current_square[2] == "right":
        if current_square[1]+1 < len(array[current_square[0]]):
            if array[current_square[0]][current_square[1]+1][0] == "#":
                current_square[2] = "down"
            else:
                if not array[current_square[0]][current_square[1]+1][2]:
                    result += check_loop(current_square,[current_square[0], current_square[1]+1])
                current_square[1] += 1
            
            if current_square[2] not in array[current_square[0]][current_square[1]][1]:
                array[current_square[0]][current_square[1]][1] += [current_square[2],]

        else:
            break
    
    elif current_square[2] == "down":
        if current_square[0]+1 < len(array):
            if array[current_square[0]+1][current_square[1]][0] == "#":
                current_square[2] = "left"
            else:
                if not array[current_square[0]+1][current_square[1]][2]:
                    result += check_loop(current_square,[current_square[0]+1, current_square[1]])
                current_square[0] += 1

            if current_square[2] not in array[current_square[0]][current_square[1]][1]:
                array[current_square[0]][current_square[1]][1] += [current_square[2],]
        else:
            break
    
    elif current_square[2] == "left":
        if current_square[1]-1 >= 0:
            if array[current_square[0]][current_square[1]-1][0] == "#":
                current_square[2] = "up"
            else:
                if not array[current_square[0]][current_square[1]-1][2]:
                    result += check_loop(current_square,[current_square[0], current_square[1]-1])
                current_square[1] -= 1

            if current_square[2] not in array[current_square[0]][current_square[1]][1]:
                array[current_square[0]][current_square[1]][1] += [current_square[2],]
                
        else:
            break

print(result)