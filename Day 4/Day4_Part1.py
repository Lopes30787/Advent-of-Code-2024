file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 4\\Day4.txt', 'r')

result = 0
array = []

for line in file:
    line_array = []

    for char in line:
        if char != "\n":
            line_array += char

    array += [line_array,]
print(array)
i = 0
def search_xmas(i,j):
    valid = 0

    if i > 2:
        # Search Up
        if array[i-1][j] == "M" and array[i-2][j] == "A" and array[i-3][j] == "S":
            valid += 1

        # Search Upwards Left Diagonal
        if j > 2:
            if array[i-1][j-1] == "M" and array[i-2][j-2] == "A" and array[i-3][j-3] == "S":
                valid += 1
        
        # Search Upwards Right Diagonal
        if j+3 < len(array[i]):
            if array[i-1][j+1] == "M" and array[i-2][j+2] == "A" and array[i-3][j+3] == "S":
                valid += 1
    
    # Search Left
    if j > 2:
        if array[i][j-1] == "M" and array[i][j-2] == "A" and array[i][j-3] == "S":
            valid += 1
    
    # Search Right
    if j+3 < len(array[i]):
        if array[i][j+1] == "M" and array[i][j+2] == "A" and array[i][j+3] == "S":
            valid += 1

    if i+3 < len(array[i]):
        # Search Down
        if array[i+1][j] == "M" and array[i+2][j] == "A" and array[i+3][j] == "S":
            valid += 1

        # Search Downwards Left Diagonal
        if j > 2:
            if array[i+1][j-1] == "M" and array[i+2][j-2] == "A" and array[i+3][j-3] == "S":
                valid += 1
        
        # Search Downwards Right Diagonal
        if j+3 < len(array[i]):
            if array[i+1][j+1] == "M" and array[i+2][j+2] == "A" and array[i+3][j+3] == "S":
                valid += 1
    return valid


while i < len(array):
    j = 0
    
    while j < len(array[i]):
        valid = False
        
        if array[i][j] == "X":
            
            valid = search_xmas(i,j)
            
            result += valid
        j += 1
    i += 1


print(result)