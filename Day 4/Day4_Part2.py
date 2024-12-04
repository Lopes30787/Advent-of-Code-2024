file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 4\\Day4.txt', 'r')

result = 0
array = []

for line in file:
    line_array = []

    for char in line:
        if char != "\n":
            line_array += char

    array += [line_array,]

i = 0

def search_x_mas(i,j):
    valid = 0

    if i > 0 and j > 0 and i+1 < len(array) and j+1 < len(array[i]):
        top_left = array[i-1][j-1]
        top_right = array[i-1][j+1]
        down_left = array[i+1][j-1]
        down_right = array[i+1][j+1]

        # Check Xs on top
        if top_left == "M" and top_right == "M" and down_left == "S" and down_right == "S":
            valid += 1

        # Check Xs on the left
        elif top_left == "M" and top_right == "S" and down_left == "M" and down_right == "S":
            valid += 1

        # Check Xs on the right
        elif top_left == "S" and top_right == "M" and down_left == "S" and down_right == "M":
            valid += 1

        # Check Xs down
        elif top_left == "S" and top_right == "S" and down_left == "M" and down_right == "M":
            valid += 1
    
    return valid


while i < len(array):
    j = 0
    
    while j < len(array[i]):
        valid = False
        
        if array[i][j] == "A":
            
            valid = search_x_mas(i,j)
            
            result += valid
        j += 1
    i += 1


print(result)