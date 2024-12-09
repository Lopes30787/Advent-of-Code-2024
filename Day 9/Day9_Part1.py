from math import floor

file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 9\\Day9.txt', 'r')

blocks = []
result = 0

for line in file:
    i = 0

    for char in line:
        if i % 2 == 0:
            blocks += [str(floor(i/2)),] * int(char)
        
        else:
            blocks += [".",] * int(char)

        i += 1

i = 0
j = len(blocks) - 1 

while True:
    if blocks[i] == ".":
        if blocks[j] != ".":
            result += i * int(blocks[j])

            i += 1
            j -= 1
        
        else:
            j-= 1

    else:
        result += i * int(blocks[i])
        i += 1

    if i >= j:
        if i == j and blocks[i] != ".":
            result += i * int(blocks[i])

        break

print(result)