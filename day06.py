"""
https://adventofcode.com/2024/day/6
"""
from util import get_puzzle_input_lines, run_file, start_timer, get_elapsed_ms
import copy


def parse_input():
    lines = get_puzzle_input_lines('day06')
    return [[cell for cell in list(l)] for l in lines]

def find_guard(map):
    for y, row in enumerate(map):
        if '^' in row:
            return row.index('^'), y

direction_changes = {
    1: 2,
    2: 3,
    3: 4,
    4: 1
}
def turn90(direction):
   global direction_changes
   return direction_changes[direction]

direction_coordinate_changes = {
        1: lambda x,y: (x, y-1),
        2: lambda x,y: (x+1, y),
        3: lambda x,y: (x, y+1),
        4: lambda x,y: (x-1, y)
    }
def next_step(cur_x, cur_y, direction):
    global direction_coordinate_changes
    return direction_coordinate_changes[direction](cur_x, cur_y)

def walk_map(the_map):
    x, y = find_guard(the_map)
    the_map[y][x] = 'X'
    direction = 1
    while True:
        nextx, nexty = next_step(x, y, direction)
        if nextx < 0 or nextx >= len(the_map[0]) or nexty < 0 or nexty >= len(the_map):
            break

        next_spot = the_map[nexty][nextx]

        if next_spot == '#':
            direction = turn90(direction)
        else:
            the_map[nexty][nextx] = 'X'
            x = nextx
            y = nexty

def part1():
    the_map = parse_input()
    walk_map(the_map)
    score = 0 # one spot for his starting position?
    for row in the_map:
        score += len([cell for cell in row if cell == 'X'])
    return score


def map_has_loop(guard_x, guard_y, the_map):
    the_map[guard_y][guard_x] = 'X'
    direction = 1

    while True:
        next_x, next_y = next_step(guard_x,guard_y, direction)

        if next_x < 0 or next_x >= len(the_map[0]) or next_y < 0 or next_y >= len(the_map):
            return False

        next_spot = the_map[next_y][next_x]

        if next_spot == '#':
            direction = turn90(direction)
        else:
            guard_x = next_x
            guard_y = next_y
            if next_spot == direction:
                return True
            else:
                the_map[next_y][next_x] = direction


def part2():
    source_map = parse_input()
    a_map = [[c for c in l] for l in source_map]
    guard_x, guard_y = find_guard(a_map)
    walk_map(a_map)
    possible_blocker_positions = []

    for y, row in enumerate(a_map):
        for x, cell in enumerate(row):
            if a_map[y][x] == 'X' and not (guard_x == x and guard_y == y):
                possible_blocker_positions.append((x, y))

    good_spots = 0
    for blocker_x, blocker_y in possible_blocker_positions:
        the_map = [[c for c in l] for l in source_map]
        the_map[blocker_y][blocker_x] = '#'
        if map_has_loop(guard_x, guard_y, the_map):
            good_spots += 1

    return good_spots

run_file()
# Day 06:
# 	Part 1: 5153  execution time: 2.3ms
# 	Part 2: 1711  execution time: 4526.1ms

