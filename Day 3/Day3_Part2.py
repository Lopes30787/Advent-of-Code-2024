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
enabled = True

do = ""
dont = ""
mul = ""



while True:
    added_mul = False
    added_do = False
    added_dont = False

    char = file.read(1) 
    if not char: 
        break

    if char == 'm' and mul == "" and enabled:
        mul += char
        added_mul = True

    elif char == 'u' and mul == "m":
        mul += char
        added_mul = True

    elif char == 'l' and mul == "mu":
        mul += char
        added_mul = True

    elif char == 'd':
        if do == "":
            do += char
            added_do = True
        if dont == "":
            dont += char
            added_dont = True

    elif char == 'o': 
        if do == "d":
            do += char
            added_do = True
        if dont == "d":
            dont += char
            added_dont = True

    elif char == 'n' and dont == "do":
        dont += char
        added_dont = True

    elif char == '\'' and dont == "don":
        dont += char
        added_dont = True

    elif char == 't' and dont == "don\'":
        dont += char
        added_dont = True

    elif char == '(':
        if mul == "mul":
            first = read_numbers(True)
            if first is not False:
                second = read_numbers(False)
                if second is not False:
                    result += first * second
        
        if do == "do":
            do += char
            added_do = True

        if dont == "don't":
            dont += char
            added_dont = True

    elif char == ')':
        if do == "do(":
            enabled = True

        if dont == "don't(":
            enabled = False

    if not added_mul:
        mul = ""
    if not added_do:
        do = ""
    if not added_dont:
        dont = ""

print(result)