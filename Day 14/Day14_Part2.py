file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 14\\Day14.txt', 'r')

num_seconds = 100

size_bathroom = [101,103]
robots_pos = []
robots_vel = []

for line in file:

    line = line.split(" ")

    position = line[0][2:].split(",")
    velocity = line[1][2:].split(",")

    if velocity[1][len(velocity[1])-1] == "\n":
        velocity[1] = velocity[1][:-1]

    robots_pos += [(int(position[0]),int(position[1])),]
    robots_vel += [(int(velocity[0]),int(velocity[1])),]

seconds = 0
while True:
    seconds += 1
    for j in range(len(robots_pos)):
        robots_pos[j] = [int(robots_pos[j][0]) + int(robots_vel[j][0]), int(robots_pos[j][1]) + int(robots_vel[j][1])]

        while robots_pos[j][0] > size_bathroom[0] - 1:
            robots_pos[j][0] -= size_bathroom[0]

        while robots_pos[j][0] < 0:
            robots_pos[j][0] += size_bathroom[0]

        while robots_pos[j][1] > size_bathroom[1] - 1:
            robots_pos[j][1] -= size_bathroom[1]

        while robots_pos[j][1] < 0:
            robots_pos[j][1] += size_bathroom[1]

        robots_pos[j] = (robots_pos[j][0],robots_pos[j][1])

    robots_set = set(robots_pos)

    if len(robots_pos) == len(robots_set):
        break

print(seconds)


