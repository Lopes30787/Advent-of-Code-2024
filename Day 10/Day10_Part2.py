file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 10\\Day10.txt', 'r')

result = 0

trail = []

for line in file:

    trail_line = []

    for char in line:
        
        if char != "\n":
            trail_line += [int(char),]
    
    trail += [trail_line,]

def check_neighbours(i, j):
    neighbours = [-1,-1,-1,-1]

    if i > 0:
        neighbours[0] = trail[i-1][j]

    if i < len(trail) - 1:
        neighbours[1] = trail[i+1][j]

    if j > 0:
        neighbours[2] = trail[i][j-1]

    if j < len(trail[i]) - 1:
        neighbours[3] = trail[i][j+1]

    return neighbours

def check_trail(i, j, current):
    neighbours = check_neighbours(i,j)

    global result

    if neighbours[0] == current+1:
        if current == 8:
            result += 1
        
        else:
            check_trail(i-1, j, current+1)

    if neighbours[1] == current+1:
        if current == 8:
            result += 1
        
        else:
            check_trail(i+1, j, current+1)

    if neighbours[2] == current+1:
        if current == 8:
            result += 1
        
        else:
            check_trail(i, j-1, current+1)

    if neighbours[3] == current+1:
        if current == 8:
            result += 1
        
        else:
            check_trail(i, j+1, current+1)

for i in range(len(trail)):
    for j in range(len(trail[0])):

        check_trail(i,j,0)

print(result)