"""
https://adventofcode.com/2024/day/6
"""
from util import get_puzzle_input_lines

def parse_input():
    lines = get_puzzle_input_lines('day06')
    return [[cell for cell in list(l)] for l in lines]

def find_guard(map):
    for y, row in enumerate(map):
        if '^' in row:
            return row.index('^'), y

def turn90(direction):
   return { 1: 2, 2: 3, 3: 4, 4: 1}[direction]

def next_step(max_x, max_y, cur_x, cur_y, direction):
    if direction == 1:
        if cur_y == 0:
            return None,None
        else:
            return cur_x, cur_y - 1
    elif direction == 2:
        if cur_x == max_x:
            return None, None
        else:
            return cur_x + 1, cur_y
    elif direction == 3:
        if cur_y == max_y:
            return None, None
        else:
            return cur_x, cur_y + 1
    else:
        if cur_x == 0:
            return None, None
        else:
            return cur_x - 1, cur_y

def walk_map(the_map):
    guard_x, guard_y = find_guard(the_map)

    max_x = len(the_map[0]) - 1
    max_y = len(the_map) -1

    direction = 1
    the_map[guard_y][guard_x] = 1

    while True:
        next_x, next_y = next_step(max_x, max_y, guard_x, guard_y, direction)
        if next_x is None:
            return False

        next_spot = the_map[next_y][next_x]

        while next_spot == '#':
            direction = turn90(direction)
            next_x, next_y = next_step(max_x, max_y, guard_x, guard_y, direction)
            if next_x is None:
                return False
            next_spot = the_map[next_y][next_x]

        guard_x = next_x
        guard_y = next_y
        if next_spot == direction:
            return True
        else:
            the_map[next_y][next_x] = direction

def part1():
    the_map = parse_input()
    walk_map(the_map)
    score = 0
    for row in the_map:
        score += len([cell for cell in row if cell in [1,2,3,4]])
    return score


def part2():
    source_map = parse_input()
    walked_map = [[c for c in l] for l in source_map]

    guard_x, guard_y = find_guard(walked_map)
    walk_map(walked_map)
    possible_blocker_positions = []

    for y, row in enumerate(walked_map):
        for x, cell in enumerate(row):
            if walked_map[y][x] in [1,2,3,4] and not (guard_x == x and guard_y == y):
                possible_blocker_positions.append((x, y))

    good_spots = 0
    for blocker_x, blocker_y in possible_blocker_positions:
        the_map = [[c for c in l] for l in source_map]
        the_map[blocker_y][blocker_x] = '#'
        if walk_map(the_map):
            good_spots += 1

    return good_spots

# Day 6 🎄
# 	Part 1: 5153              execution time: 2.3ms
# 	Part 2: 1711              execution time: 3602.1ms


