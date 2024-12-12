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

def calculate_sides(garden):
    external_sides = []
    sides = 0
    for i,j in garden:

        up = [i-1,j] in garden 
        left = [i,j-1] in garden
        down = [i+1,j] in garden
        right = [i,j+1] in garden

        if not up and not left:  
            sides+=1
        if not left and not down:
            sides+=1
        if not down and not right:
            sides+=1
        if not right and not up:
            sides+=1

        if not up:
            if [i-1,j-1] in garden and left:
                if [i-1,j-1,i,j] not in external_sides:
                    external_sides += [[i-1,j-1,i,j],]
                    sides += 1
            
            if [i-1, j+1] in garden and right:
                if [i,j,i-1,j+1] not in external_sides:
                    external_sides += [[i,j,i-1,j+1],]
                    sides += 1

        if not right:
            
            if [i-1, j+1] in garden and up:
                if [i-1,j+1,i,j] not in external_sides:
                    external_sides += [[i-1,j+1,i,j],]
                    sides += 1
        
            if [i+1, j+1] in garden and down:
                if [i,j,i+1,j+1] not in external_sides:
                    external_sides += [[i,j,i+1,j+1],]
                    sides += 1

        if not down:
            if [i+1, j-1] in garden and left:
                if [i,j,i+1,j-1] not in external_sides:
                    external_sides += [[i,j,i+1,j-1],]
                    sides += 1

            if [i+1, j+1] in garden and right:
                if [i+1,j+1,i,j] not in external_sides:
                    external_sides += [[i+1,j+1,i,j],]
                    sides += 1
        
        if not left:
            if [i-1, j-1] in garden and up:
                if [i,j,i-1,j-1] not in external_sides:
                    external_sides += [[i,j,i-1,j-1],]
                    sides += 1
            if [i+1, j-1] in garden and down:
                if [i+1,j-1,i,j] not in external_sides:
                    external_sides += [[i+1,j-1,i,j],]
                    sides += 1

    return sides


def check_garden(i, j):
    
    stack = [[i,j],]

    global checked 
    global garden

    garden_checked = []

    letter = garden[i][j]

    checked += [[i,j],]
    garden_checked += [[i,j],]

    while len(stack) > 0:
        current = stack.pop()

        neighbours = check_neighbours(current[0], current[1])

        if neighbours[0] == letter and [current[0]-1,current[1]] not in garden_checked:
            stack += [[current[0]-1,current[1]],]
            checked += [[current[0]-1,current[1]],]
            garden_checked += [[current[0]-1,current[1]],]

        if neighbours[1] == letter and [current[0]+1,current[1]] not in garden_checked:
            stack += [[current[0]+1,current[1]],]
            checked += [[current[0]+1,current[1]],]
            garden_checked += [[current[0]+1,current[1]],]

        if neighbours[2] == letter and [current[0],current[1]-1] not in garden_checked:
            stack += [[current[0],current[1]-1],]
            checked += [[current[0],current[1]-1],]
            garden_checked += [[current[0],current[1]-1],]

        if neighbours[3] == letter and[current[0],current[1]+1] not in garden_checked:
            stack += [[current[0],current[1]+1],]
            checked += [[current[0],current[1]+1],]
            garden_checked += [[current[0],current[1]+1],]

    sides = calculate_sides(garden_checked)

    return len(garden_checked) * sides


for i in range(len(garden)):
    for j in range(len(garden[i])):

        if [i,j] in checked:
            continue

        price += check_garden(i, j)

print(price)