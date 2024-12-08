file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 8\\Day8.txt', 'r')

antennas = {}

size_file = -1
for line in file:
    size_file += 1
    size_line = -1
    for char in line:
        size_line += 1

        if char != "." and char != "\n":
            if char not in antennas.keys():
                antennas[char] = [[size_file, size_line],]

            else:
                antennas.update({char: antennas[char] + [[size_file, size_line],]})

points = []
def check_points(first, second, points):

    diff_dist = [first[0] - second[0], first[1] - second[1]]

    point_1 = [first[0] + diff_dist[0], first[1] + diff_dist[1]]
    point_2 = [second[0] - diff_dist[0], second[1] - diff_dist[1]]

    if point_1[0] >= 0 and point_1[0] <= size_file and point_1[1] >= 0 and point_1[1] <= size_line and point_1 not in points:
        points += [point_1,]

    if point_2[0] >= 0 and point_2[0] <= size_file and point_2[1] >= 0 and point_2[1] <= size_line and point_2 not in points:
        points += [point_2,]

    return points

for key in antennas.keys():
    values = antennas[key]

    for i in range(len(values)):
        for j in range(i+1, len(values)):
            points = check_points(values[i], values[j], points)

print(len(points))