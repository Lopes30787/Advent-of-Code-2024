file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code\\Day 3\\Day3.txt', 'r')

def read_numbers(first):
    number = ""
    valid = False
    while True:
        char = file.read(1) 
        if not char: 
            break

        if char.isdigit():
            number += char

        elif char == ',':
            if first and len(number) != 0:
                valid = True
            break

        elif char == ')':
            if not first and len(number) != 0:
                valid = True
            break

        else:
            valid = False
            break
    if valid:
        return int(number)
    return valid

result = 0
while True:
    char = file.read(1) 
    if not char: 
        break

    if char == 'm':
        char = file.read(1) 
        if char == 'u':
            char = file.read(1) 
            if char == 'l':
                char = file.read(1) 
                if char == '(':
                    first = read_numbers(True)
                    if first is not False:
                        second = read_numbers(False)
                        if second is not False:
                            result += first * second

print(result)