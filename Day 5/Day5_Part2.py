from math import floor

file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 5\\Day5.txt', 'r')

result = 0

lines = file.readlines()
rules = []

i = 0
while True:
    first_number = ""
    second_number = ""

    line = lines[i]

    if len(line) == 1:
        i += 1
        break

    j = -1
    while True:
        j += 1
        if line[j].isdigit():
            first_number += line[j]
        
        else:
            break

    while True:
        j += 1
        if line[j].isdigit():
            second_number += line[j]

        else:
            break
    
    rules += [[first_number, second_number],]
    i += 1

while i < len(lines):
    line = lines[i]
    if line[len(line)-1] == "\n":
        line = line[:-1]
    line = line.split(",")

    valid = True
    
    for rule in rules:
        second = False
        for number in line:
            if number == rule[0] and second:
                valid = False
                break
            
            elif number == rule[1]:
                second = True

    if not valid:    
        while True:
            new_valid = True
            for rule in rules:
                second = -1
                for k in range(len(line)):
                    if line[k] == rule[0] and second != -1:
                        new_valid = False
                        line[k] = rule[1]
                        line[second] = rule[0]
                        break
                    
                    elif line[k] == rule[1]:
                        second = k
            
            if new_valid:
                break

        result += int(line[floor(len(line)/2)])
    
    i += 1

print(result)