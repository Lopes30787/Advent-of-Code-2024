file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 6\\Day6.txt', 'r')

array = []

current_square = []
direction = "up"

i = 0
for line in file:
    line_array = []
    j = 0

    for char in line:
        if char == "#":
            line_array += char
        elif char == "^":
            line_array += "."
            current_square = [i,j]
        elif char == ">":
            line_array += "."
            current_square = [i,j]
            direction = "right"
        elif char == "v":
            line_array += "."
            current_square = [i,j]
            direction = "down"
        elif char == "<":
            line_array += "."
            current_square = [i,j]
            direction = "left"
        elif char != "\n":
            line_array += "."
        j += 1
    
    i += 1
    array += [line_array,]

explored_spaces = [current_square,]

while True:
    if direction == "up":
        if current_square[0]-1 >= 0:
            if array[current_square[0]-1][current_square[1]] == "#":
                direction = "right"
            else:
                current_square = [current_square[0]-1,current_square[1]]
                if current_square not in explored_spaces:
                    explored_spaces += [current_square,]
        else:
            break
    
    elif direction == "right":
        if current_square[1]+1 < len(array[current_square[0]]):
            if array[current_square[0]][current_square[1]+1] == "#":
                direction = "down"
            else:
                current_square = [current_square[0],current_square[1]+1]
                if current_square not in explored_spaces:
                    explored_spaces += [current_square,]
        else:
            break
    
    elif direction == "down":
        if current_square[0]+1 < len(array):
            if array[current_square[0]+1][current_square[1]] == "#":
                direction = "left"
            else:
                current_square = [current_square[0]+1,current_square[1]]
                if current_square not in explored_spaces:
                    explored_spaces += [current_square,]
        else:
            break
    
    elif direction == "left":
        if current_square[1]-1 >= 0:
            if array[current_square[0]][current_square[1]-1] == "#":
                direction = "up"
            else:
                current_square = [current_square[0],current_square[1]-1]
                if current_square not in explored_spaces:
                    explored_spaces += [current_square,]
        else:
            break


print(len(explored_spaces))