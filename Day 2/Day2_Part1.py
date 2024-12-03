file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 2\\Day2.txt', 'r')

safe = 0
increasing = True

for line in file:
    is_safe = True
    line = line.split()
    for i in range(len(line)-1):

        difference = int(line[i]) - int(line[i+1])

        if i == 0:
            if difference > 0:
                increasing = True
            else:
                increasing = False

        if abs(difference) > 3 or difference == 0:
            is_safe = False
            break

        if increasing and difference < 0:
            is_safe = False
            break

        if not increasing and difference > 0:
            is_safe = False
            break

    if is_safe:
        safe += 1

print(safe)