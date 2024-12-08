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

    i = 0
    while True:
        point = [first[0] + diff_dist[0] * i, first[1] + diff_dist[1] * i]

        if point[0] >= 0 and point[0] <= size_file and point[1] >= 0 and point[1] <= size_line:
            if point not in points:
                points += [point,]
            i += 1
        
        else:
            break

    i = 0
    while True:
        point = [second[0] - diff_dist[0] * i, second[1] - diff_dist[1] * i]

        if point[0] >= 0 and point[0] <= size_file and point[1] >= 0 and point[1] <= size_line:
            if point not in points:
                points += [point,]
            i += 1
        
        else:
            break
    
    return points

for key in antennas.keys():
    values = antennas[key]

    for i in range(len(values)):
        for j in range(i+1, len(values)):
            points = check_points(values[i], values[j], points)

print(len(points))