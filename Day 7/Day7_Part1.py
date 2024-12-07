file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 7\\Day7.txt', 'r')

possible = 0

def check_calculation(result, numbers, operations, last_x):
    res = numbers[0]

    next_last_x = -1

    for i in range(1, len(numbers)):
        if operations[i-1] == "x":
            res *= numbers[i]
            if i-1 >= last_x:
                operations[i-1] = "+"
            else:
                next_last_x = i-1

        else:
            res += numbers[i]
            if i-1 >= last_x:
                operations[i-1] = "x"
                next_last_x = i-1
  
    if res == result:
        return True, operations, next_last_x
    
    return False, operations, next_last_x


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

    res, operations, last_next_x = check_calculation(result, numbers, ["x"] * (len(numbers)-1), len(numbers)-2)

    if not res:
        while True:
            if last_next_x != -1:
                res, operations, last_next_x = check_calculation(result, numbers, operations, last_next_x)
                
                if res:
                    break
            
            else:
                res, operations, last_next_x = check_calculation(result, numbers, ["+"] * (len(numbers)-1), -1)
                break
    
    if res:
        possible += result

print(possible)