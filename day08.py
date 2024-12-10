"""
https://adventofcode.com/2024/day/8
"""
from util import get_puzzle_input_lines, run_file

def parse_input():
    lines = get_puzzle_input_lines('day08')
    records = {}
    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            if cell == '.':
                continue
            if cell not in records:
                records[cell] = []
            records[cell].append((x,y))

    max_x = len(lines[0]) - 1
    max_y = len(lines) - 1
    return records, max_x, max_y

def part1():
    records, max_x, max_y = parse_input()
    anti_nodes = []
    for freq, coordinates in records.items():
        for src in coordinates:
            for dest in [coordinate for coordinate in coordinates if coordinate != src]:
                x_diff = dest[0] - src[0]
                y_diff = dest[1] - src[1]
                new_anti_nodes = [
                    (src[0] - x_diff, src[1] - y_diff),
                    (dest[0] + x_diff, dest[1] + y_diff)
                ]

                for node in new_anti_nodes:
                    if 0 <= node[0] <= max_x and 0 <= node[1] <= max_y:
                        node_str = f'{node[0],node[1]}'
                        if node_str not in anti_nodes:
                            anti_nodes.append(node_str)
    return len(anti_nodes)

def part2():
    records, max_x, max_y = parse_input()

    def is_int(num):
        return abs(num - round(num)) < .00001

    def x_is_okay(x):
        return 0 <= x <= max_x

    def y_is_okay(y):
        return 0 <= y <= max_y

    def is_okay(coordinates_to_compare):
        return x_is_okay(coordinates_to_compare[0]) and y_is_okay(coordinates_to_compare[1])


    antinodes = []
    for freq, coordinates in records.items():
        for src in coordinates:
            other_coordinates = [coordinate for coordinate in coordinates if coordinate != src]
            for dest in other_coordinates:
                x_diff = dest[0] - src[0]
                y_diff = dest[1] - src[1]

                if x_diff == 0:
                    x = src[0]
                    for y in range(max_y+1):
                        if is_okay((x,y)): # not coords_equal((x,y), src) and not coords_equal((x,y), dest) and
                            antinode_str = f'{x},{y}'
                            if antinode_str not in antinodes:
                                antinodes.append(antinode_str)
                    continue


                slope = y_diff / x_diff

                x, y = src
                while is_okay((x,y)):
                    if is_int(y):
                        antinode_str = f'{x},{y}'
                        if antinode_str not in antinodes:
                            antinodes.append(antinode_str)

                    x -= 1
                    y -= slope

                    if is_int(y):
                        y = round(y)

                x, y = src
                while is_okay((x,y)):
                    if is_int(y):
                        antinode_str = f'{x},{y}'
                        if antinode_str not in antinodes:
                            antinodes.append(antinode_str)
                    x += 1
                    y += slope

                    if is_int(y):
                        y = round(y)

    return len(antinodes)

run_file()
# Day 8:
# 	Part 1: 273  execution time: 2.1ms
# 	Part 2: 1017  execution time: 24.3ms
