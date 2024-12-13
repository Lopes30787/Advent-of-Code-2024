file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 13\\Day13.txt', 'r')

games = []
fewest_tokens = 0

current = [0,0,0]
for line in file:

    line = line.split(" ")

    if len(line) == 4: 
        if line[1][0] == "A":
            j = 0
        
        elif line[1][0] == "B":
            j = 1

        current[j] = [int(line[2][2:-1]), int(line[3][2:-1])]

    elif len(line) == 3:
        current[2] = [int(line[1][2:-1]), int(line[2][2:-1])]
        games += [current.copy(),]
games[len(games)-1][2][1] = int(line[2][2:])

for game in games:

    j = round((((game[2][1]*game[0][0]) / game[0][1]) - game[2][0]) / (-game[1][0] + (game[1][1]/game[0][1] *game[0][0])))
    k = round((game[2][0] - j * game[1][0]) / game[0][0])

    if k* game[0][0] + j * game[1][0] == game[2][0] and k* game[0][1] + j * game[1][1] == game[2][1]:
        fewest_tokens += 3*k + j

print(fewest_tokens)