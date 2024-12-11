from functools import cache

file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2024\\Day 11\\Day11.txt', 'r')

stones = []

for line in file:

    stones = line.split(" ")

for i in range(len(stones)):
    stones[i] = int(stones[i])

@cache
def count_stones(stone, blinks):
    if blinks == 0:
        return 1
    
    elif stone == 0:
        return count_stones(1, blinks-1)
    
    elif len(str(stone)) % 2 == 0:
        exp = len(str(stone)) / 2

        return count_stones(int(stone // (10 ** exp)) , blinks -1) + count_stones(int(stone % (10 ** exp)), blinks -1)

    else:
        return count_stones(stone * 2024, blinks -1)

print(sum(count_stones(stone, 75) for stone in stones))