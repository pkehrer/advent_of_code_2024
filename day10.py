"""
https://adventofcode.com/2024/day/10
"""

from util import get_puzzle_input_lines, run_file


# list of lists of ints parsed from single digit characters
def parse_input():
    lines = get_puzzle_input_lines('day10')
    return [[-1 if cell == '.' else int(cell) for cell in list(line)] for line in lines]

def print_map(a_map):
    for line in a_map:
        for cell in line:
            print('.' if cell == -1 else cell, end='')
        print()

# return list of (x,y) tuples of the coordinates of every '0' on the map
def find_zero_coordinates(the_map):
    zero_coordinates = []
    for y, row in enumerate(the_map):
        for x, cell in enumerate(row):
            if cell == 0:
                zero_coordinates.append((x, y))
    return zero_coordinates

# get the value in the map at the coordinates
def lookup(a_map, coordinates):
    return a_map[coordinates[1]][coordinates[0]]

# return all surrounding coordinates, excluding spots that go off the mmap
def get_surrounding_coordinates(the_map, c):
    all_spots= [(c[0], c[1] - 1),
                (c[0] + 1, c[1]),
                (c[0], c[1] + 1),
                (c[0] - 1, c[1])]
    returned = []
    for spot in all_spots:
        if 0 <= spot[0] <= (len(the_map[0]) - 1) and 0 <= spot[1] <= (len(the_map) - 1):
            returned.append(spot)
    return returned

# return a list of all possible trails from the current coordinates (recursive)
def find_trails(the_map, current_coordinates, previous_spots = None):
    if previous_spots is None:
        previous_spots = []

    current_value = lookup(the_map, current_coordinates)
    if current_value == 9:
        return [previous_spots + [current_coordinates]]
    else:
        possible_trails = []
        for possible_next_spot in get_surrounding_coordinates(the_map, current_coordinates):
            next_value = lookup(the_map, possible_next_spot)
            if next_value == current_value + 1:
                further_trails = find_trails(the_map, possible_next_spot, previous_spots + [current_coordinates])
                possible_trails.extend(further_trails)
        return possible_trails

def part1():
    answer = 0
    the_map = parse_input()

    for zero_x, zero_y in find_zero_coordinates(the_map):
        all_trails = find_trails(the_map, (zero_x, zero_y))
        # keep the end locations in a set so we can count the distinct end points instead of trails
        trail_ends = set()
        for trail in all_trails:
            if len(trail) == 10:
                trail_ends.add(trail[-1])

        answer += len(trail_ends)

    return answer
    
def part2():
    answer = 0
    the_map = parse_input()

    zero_coordinates = []
    for y, row in enumerate(the_map):
        for x, cell in enumerate(row):
            if cell == 0:
                zero_coordinates.append((x, y))

    for zero_x, zero_y in zero_coordinates:
        all_trails = find_trails(the_map, (zero_x, zero_y))
        for trail in all_trails:
            # part 2 calls for all distinct trails (actually easier luckily)
            if len(trail) == 10:
                answer += 1

    return answer

run_file()
# Day 10:
# 	Part 1: 646  execution time: 10.8ms
# 	Part 2: 1494  execution time: 9.5ms

