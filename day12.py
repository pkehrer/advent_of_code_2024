"""
https://adventofcode.com/2024/day/12
"""
from util import get_puzzle_input_lines, increment_dict


def parse_input():
    lines = get_puzzle_input_lines('day12')
    return [[cell for cell in list(l)] for l in lines]

def enumerate_map(the_map):
    for y, row in enumerate(the_map):
        for x, cell in enumerate(row):
            yield x,y

def print_map(the_map):
    for row in the_map:
        for cell in row:
            print(cell, end='')
        print()

def is_on_map(coordinates, a_map):
    max_x = len(a_map[0]) - 1
    max_y = len(a_map) - 1
    return 0 <= coordinates[0] <= max_x and 0 <= coordinates[1] <= max_y

def get_plot(coordinates, a_map):
    return a_map[coordinates[1]][coordinates[0]]

def get_adjacent_coordinates_on_map(coordinates, a_map, plot_type):
    def matches_and_is_on_map(adjacent_coordinates):
        return (is_on_map(adjacent_coordinates, a_map)
                and get_plot(adjacent_coordinates, a_map) == plot_type)

    return [adjacent for adjacent in get_adjacent_coordinates(coordinates) if matches_and_is_on_map(adjacent)]

def get_adjacent_coordinates(coordinates):
    x,y = coordinates
    return [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]

def explore_region(current_coordinate, the_map, plot_type = None, visited_coordinates = None):
    if visited_coordinates is None:
        visited_coordinates = set()

    if plot_type is None:
        plot_type = get_plot(current_coordinate, the_map)

    visited_coordinates.add(current_coordinate)

    for adjacent_coordinates in get_adjacent_coordinates_on_map(current_coordinate, the_map, plot_type):
        if adjacent_coordinates not in visited_coordinates:
            explore_region(adjacent_coordinates, the_map, plot_type, visited_coordinates)

    return plot_type, visited_coordinates

def get_perimeter(region_coordinates):
    sides = 0
    for coordinate in region_coordinates:
        for adjacent in get_adjacent_coordinates(coordinate):
            if adjacent not in region_coordinates:
                sides += 1
    return sides

def next_coordinate_in_direction(coordinate, direction, length = 1):
    x,y = coordinate
    if direction == 0:
        return x, y - length
    elif direction == 1:
        return x + length, y
    elif direction == 2:
        return x, y + length
    elif direction == 3:
        return x - length,y
    raise ValueError('What???')

def short_perimeter(region_coordinates):
    side_spaces = [
        [], # 0: up
        [], # 1: right
        [], # 2: down
        []  # 3: left
    ]

    for coordinate in region_coordinates:
        for adjacent in get_adjacent_coordinates(coordinate):
            if adjacent not in region_coordinates:
                if adjacent[0] == coordinate[0]:
                    if adjacent[1] > coordinate[1]:
                        side_spaces[2].append(adjacent)
                    else:
                        side_spaces[0].append(adjacent)
                else:
                    if adjacent[0] > coordinate[0]:
                        side_spaces[1].append(adjacent)
                    else:
                        side_spaces[3].append(adjacent)

    side_count = 0

    for direction, spaces in enumerate(side_spaces):
        perpendicular = (direction + 1) % 4
        while len(spaces) > 0:
            coordinate = spaces[0]
            spaces.remove(coordinate)

            for magnitude in [1, -1]:
                length = 1
                next_space = next_coordinate_in_direction(coordinate, perpendicular, length * magnitude)
                while next_space in spaces:
                    spaces.remove(next_space)
                    length += 1
                    next_space = next_coordinate_in_direction(coordinate, perpendicular, length * magnitude)

            side_count += 1

    return side_count


def part1():
    the_map = parse_input()

    visited_coordinates = set()
    price = 0

    for coordinates in enumerate_map(the_map):
        if coordinates not in visited_coordinates:
            region_type, coordinates_in_region = explore_region(coordinates, the_map)
            price += len(coordinates_in_region) * get_perimeter(coordinates_in_region)
            for coordinate in coordinates_in_region:
                visited_coordinates.add(coordinate)

    return price
    
def part2():
    the_map = parse_input()

    visited_coordinates = set()
    price = 0

    for current_coordinates in enumerate_map(the_map):
        if current_coordinates not in visited_coordinates:
            region_type, coordinates_in_region = explore_region(current_coordinates, the_map)
            price += len(coordinates_in_region) * short_perimeter(coordinates_in_region)

            for coordinate in coordinates_in_region:
                visited_coordinates.add(coordinate)

    return price

# Day 12 🎄
# 	Part 1: 1550156           execution time: 41.0ms
# 	Part 2: 946084            execution time: 42.2ms
