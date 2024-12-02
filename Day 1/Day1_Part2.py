file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code\\Day 1\\Day1.txt', 'r')

first_column = []
second_column = []

for line in file:
    line = line.split()
    first_column += [line[0],]
    second_column += [line[1],]

file.close()

first_column.sort()
second_column.sort()

similarity_score = 0
j=0
for i in range(len(first_column)):
    equal = 0
    while int(first_column[i]) > int(second_column[j]):
        if j < len(second_column)-1:
            j += 1
        else:
            break
    
    while int(first_column[i]) == int(second_column[j]):
        equal += 1
        if j < len(second_column)-1:
            j += 1
        else:
            break 
    
    similarity_score += int(first_column[i]) * equal

print(similarity_score)

