file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 2\\Day2.txt', 'r')

safe = 0
increasing = True

for line in file:
    line = line.split()

    possible_reports = []
    for i in range(len(line)):
        new_line = line.copy()
        del new_line[i]
        possible_reports += [new_line,]
    print(possible_reports)
    for report in possible_reports:
        is_safe = True
        for i in range(len(report)-1):

            difference = int(report[i]) - int(report[i+1])

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
            break

    if is_safe:
        safe += 1

print(safe)