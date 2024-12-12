file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 12\\Day12.txt', 'r')

garden = []
checked = []
price = 0

for line in file:
    garden_line = []

    for char in line:
        if char != "\n":
            garden_line += char

    garden += [garden_line,]

def check_neighbours(i, j):
    neighbours = [-1,-1,-1,-1]

    if i > 0:
        neighbours[0] = garden[i-1][j]

    if i < len(garden) - 1:
        neighbours[1] = garden[i+1][j]

    if j > 0:
        neighbours[2] = garden[i][j-1]

    if j < len(garden[i]) - 1:
        neighbours[3] = garden[i][j+1]

    return neighbours

def check_garden(i, j):
    
    stack = [[i,j],]

    global checked 
    global garden

    garden_checked = []

    letter = garden[i][j]

    perimeter = 0

    checked += [[i,j],]
    garden_checked += [[i,j],]

    while len(stack) > 0:
        current = stack.pop()

        neighbours = check_neighbours(current[0], current[1])

        if neighbours[0] == letter:
            if [current[0]-1,current[1]] not in garden_checked:
                stack += [[current[0]-1,current[1]],]
                checked += [[current[0]-1,current[1]],]
                garden_checked += [[current[0]-1,current[1]],]
        else:
            perimeter += 1

        if neighbours[1] == letter: 
            if [current[0]+1,current[1]] not in garden_checked:
                stack += [[current[0]+1,current[1]],]
                checked += [[current[0]+1,current[1]],]
                garden_checked += [[current[0]+1,current[1]],]
        else:
            perimeter += 1

        if neighbours[2] == letter:
            if [current[0],current[1]-1] not in garden_checked:
                stack += [[current[0],current[1]-1],]
                checked += [[current[0],current[1]-1],]
                garden_checked += [[current[0],current[1]-1],]
        else:
            perimeter += 1

        if neighbours[3] == letter:
            if [current[0],current[1]+1] not in garden_checked:
                stack += [[current[0],current[1]+1],]
                checked += [[current[0],current[1]+1],]
                garden_checked += [[current[0],current[1]+1],]
        else:
            perimeter += 1

    return len(garden_checked) * perimeter


for i in range(len(garden)):
    for j in range(len(garden[i])):

        if [i,j] in checked:
            continue

        price += check_garden(i, j)

print(price)