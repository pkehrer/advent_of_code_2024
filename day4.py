"""
https://adventofcode.com/2024/day/4
"""
from util import get_puzzle_input_lines, run_file


def parse_input():
    lines = get_puzzle_input_lines('day4')
    return [list(record) for record in lines]

def get_coordinates_for_letter(records, letter_to_find):
    coordinates = []
    for y, record in enumerate(records):
        for x, letter in enumerate(record):
            if letter == letter_to_find:
                coordinates.append((x, y))
    return coordinates

def check_next(records, coordinates, direction, distance, letter):
    next_x = coordinates[0]
    next_y = coordinates[1]

    if direction in ["U", "UR", "UL"]:
        next_y -= distance

    if direction in ["UR", "R", "DR"]:
        next_x += distance

    if direction in ["D", "DR", "DL"]:
        next_y += distance

    if direction in ["L", "DL", "UL"]:
        next_x -= distance

    if next_x < 0 or next_y < 0 or next_x >= len(records[0]) or next_y >= len(records):
        return False

    return records[next_y][next_x] == letter


def part1():
    xmas_count = 0
    records = parse_input()
    x_coordinates = get_coordinates_for_letter(records, 'X')
    for x,y in x_coordinates:
        for direction in ["U", "UR", "R", "DR", "D", "DL", "L", "UL"]:
            is_xmas = True
            for i, next_letter in enumerate(list('MAS')):
                if not check_next(records, (x,y), direction, i + 1, next_letter):
                    is_xmas = False
            if is_xmas:
                xmas_count += 1

    return xmas_count

def part2():
    x_mas_count = 0
    records = parse_input()
    a_coordinates = get_coordinates_for_letter(records, 'A')
    for x,y in a_coordinates:
        x_mas_count_on_letter = 0
        for direction in ["UR", "DR", "DL", "UL"]:
            if check_next(records, (x,y), direction, 1, 'S') and check_next(records,(x,y), direction, -1, 'M'):
                x_mas_count_on_letter += 1
        if x_mas_count_on_letter == 2:
            x_mas_count += 1
        if x_mas_count_on_letter > 2:
            print(x_mas_count_on_letter)

    return x_mas_count

run_file()
# Day 4:
# 	Part 1: 2530  execution time: 34.9ms
# 	Part 2: 1921  execution time: 8.3ms
