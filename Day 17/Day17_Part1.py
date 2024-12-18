file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 17\\Day17.txt', 'r')

A = 0
B = 0
C = 0

for line in file:
    if line == "\n":
        break

    else:
        line = line.split(" ")
        if line[1] == "A:":
            A = int(line[2])
        elif line[1] == "B:":
            B = int(line[2])
        elif line[1] == "C:":
            C = int(line[2])

def get_combo(char):
    if char == 4:
        return A
    elif char == 5:
        return B
    elif char == 6:
        return C
    return char

operand = -1
out = ""

instructions = []
for line in file:
    for char in line:
        if char.isdigit():
            instructions += char

i = 0
while i < len(instructions):
    if operand == -1:
        operand = int(instructions[i])

    else:
        if operand == 0:
            combo = get_combo(int(instructions[i]))

            A = int(A / (2**combo))

        elif operand == 1:
            B = B ^ int(instructions[i])

        elif operand == 2:
            combo = get_combo(int(instructions[i]))
            B = combo % 8

        elif operand == 3:
            if A != 0:
                i = int(instructions[i]) -1

        elif operand == 4:
            B = B ^ C

        elif operand == 5:
            combo = get_combo(int(instructions[i]))
            out += str(combo % 8) +","

        elif operand == 6:
            combo = get_combo(int(instructions[i]))

            B = int(A / (2**combo))

        elif operand == 7:
            combo = get_combo(int(instructions[i]))

            C = int(A / (2**combo))
        
        operand = -1
    i += 1

print(out[:-1])