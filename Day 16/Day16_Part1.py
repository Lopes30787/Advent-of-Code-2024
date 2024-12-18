file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 16\\Day16.txt', 'r')

maze = []
start = []

lowest_score = -1

i = 0
for line in file:
    if line == "\n":
        break
    
    row = []
    
    j = 0
    for char in line:        
        if char == "S":
            start = [i,j]

        if char != "\n":
            if char == ".":
                row += [-1]
            else:
                row += char

        j += 1


    maze += [row,]
    i += 1

def check_adjacent(i, j):
    adjacent = [-1,-1,-1,-1]

    if i > 0:
        adjacent[0] = maze[i-1][j]

    if j < len(maze[i]) - 1:
        adjacent[1] = maze[i][j+1]

    if i < len(maze) - 1:
        adjacent[2] = maze[i+1][j]

    if j > 0:
        adjacent[3] = maze[i][j-1]

    return adjacent

def find_shortest_path(start):
    shortest_path = -1

    global maze

    stack = [[start, [start,], 1, 0],]

    while stack != []:
        start, visited, direction, score = stack.pop(0)

        adjacent = check_adjacent(start[0], start[1])

        for i in range(len(adjacent)):

            next = []
            if i == 0:
                next = [start[0] - 1, start[1]]
            elif i == 1:
                next = [start[0], start[1] + 1]
            elif i == 2:
                next = [start[0] + 1, start[1]]
            elif i == 3:
                next = [start[0], start[1] - 1]

            if type(adjacent[i]) is int:
                if direction == i and (adjacent[i] == -1 or adjacent[i] > score + 1):
                    maze[next[0]][next[1]] = score + 1
                    stack += [[next, visited, i, score + 1],]

                elif direction != i:
                    scorediff = 1001
                    if abs(i - direction) == 2:
                        scorediff = 2001

                    if adjacent[i] == -1 or adjacent[i] > score + scorediff:
                        maze[next[0]][next[1]] = score + scorediff
                        stack += [[next, visited, i, score + scorediff],]
            
            elif adjacent[i] == "E":
                scorediff = 1001
                if abs(i - direction) == 2:
                    scorediff = 2001
                elif i == direction:
                    scorediff = 1
                
                if shortest_path == -1 or score + scorediff < shortest_path:
                    shortest_path = score + scorediff

    return shortest_path

print(find_shortest_path(start))
