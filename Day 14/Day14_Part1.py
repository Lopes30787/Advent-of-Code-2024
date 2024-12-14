file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 14\\Day14.txt', 'r')

quadrants = [0,0,0,0]

size_bathroom = [101,103]
num_seconds = 100

for line in file:

    line = line.split(" ")

    position = line[0][2:].split(",")
    velocity = line[1][2:].split(",")

    if velocity[1][len(velocity[1])-1] == "\n":
        velocity[1] = velocity[1][:-1]

    position = [int(position[0]) + int(velocity[0]) * num_seconds, int(position[1]) + int(velocity[1]) * num_seconds]

    while position[0] > size_bathroom[0] - 1:
        position[0] -= size_bathroom[0]

    while position[0] < 0:
        position[0] += size_bathroom[0]

    while position[1] > size_bathroom[1] - 1:
        position[1] -= size_bathroom[1]

    while position[1] < 0:
        position[1] += size_bathroom[1]

    if position[0] < (size_bathroom[0]-1) / 2:
        if position[1] < (size_bathroom[1]-1) / 2:
            quadrants[0] += 1

        elif position[1] > (size_bathroom[1]-1) / 2:
            quadrants[1] += 1

    if position[0] > (size_bathroom[0]-1) / 2:
        if position[1] < (size_bathroom[1]-1) / 2:
            quadrants[2] += 1

        elif position[1] > (size_bathroom[1]-1) / 2:
            quadrants[3] += 1

print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])