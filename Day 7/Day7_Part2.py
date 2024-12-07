file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 7\\Day7.txt', 'r')

possible = 0
alter = True

def check_calculation(result, numbers, operations):
    res = numbers[0]

    all_concat = True
    alter = True

    for i in range(1, len(numbers)):
        if operations[i-1] == "x":
            all_concat = False
            res *= numbers[i]

        elif operations[i-1] == "+":
            all_concat = False
            res += numbers[i]

        else:
            res = int(str(res) + str(numbers[i]))

    if operations[len(operations)-1] == "|":
        operations[len(operations)-1] = "x"
            
    elif operations[len(operations)-1] == "x":
        operations[len(operations)-1] = "+"
        alter = False
            
    else:
        operations[len(operations)-1] = "|"    
        alter = False        

    for i in range(len(operations)-2, -1, -1):
        if alter:
            if operations[i] == "|":
                operations[i] = "x"
                
            elif operations[i] == "x":
                operations[i] = "+"
                alter = False
                    
            else:
                operations[i] = "|"
                alter = False
        else:
            break

    if res == result:
        return True, operations, all_concat
    
    return False, operations, all_concat


for line in file:
    result = 0
    numbers = []
    current = ""

    for char in line:
        if char.isdigit():
            current += char
        elif char == ":":
            result = int(current)
            current = ""
        elif current != "":
            numbers += [int(current),]
            current = ""

    if current != "":
            numbers += [int(current),]

    res, operations, all_concat = check_calculation(result, numbers, ["x"] * (len(numbers)-1))

    if not res:
        while True:
            if not all_concat:
                res, operations, all_concat = check_calculation(result, numbers, operations)
                
                if res:
                    break
            
            else:
                break
    
    if res:
        possible += result

print(possible)