from math import floor

file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 9\\Day9.txt', 'r')

blocks = []
result = 0

for line in file:
    i = 0

    for char in line:
        if i % 2 == 0:
            blocks += [[str(floor(i/2))] * int(char),]
        
        else:
            if int(char) != 0:
                blocks += [["."] * int(char),]

        i += 1

i = 0
j = len(blocks) - 1 

while True:
    if j < 0:
        break

    if i >= len(blocks):
        i = 0
        j -= 1
    
    if blocks[i][0] == ".":
        if blocks[j][0] != ".":
            if len(blocks[j]) == len(blocks[i]) and j > i:

                blocks[i] = [blocks[j][0]] * len(blocks[j])
                blocks[j] = ["."] * len(blocks[j])
                j -= 1
                i = 0

            elif len(blocks[j]) < len(blocks[i]) and j > i:
                blocks = blocks[0:i] + [[blocks[j][0]] * len(blocks[j]),] + [["."] * (len(blocks[i]) - len(blocks[j])),] + blocks[i+1:]
                
                blocks[j+1] = ["."] * len(blocks[j+1])
                i = 0

            else:
                i += 1
        else:
            j -= 1

    else:
        i += 1

j = 0
for i in range(len(blocks)):
    if blocks[i][0] == ".":
        j += len(blocks[i])

    else:
        for k in range(len(blocks[i])):
            result += int(blocks[i][0]) * j

            j += 1

print(result)