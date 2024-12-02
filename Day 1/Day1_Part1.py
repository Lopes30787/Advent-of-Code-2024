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
print(len(first_column))
sum = 0
for i in range(len(first_column)):
    sum += abs(int(first_column[i]) - int(second_column[i]))

print(sum)

