"""
https://adventofcode.com/2024/day/9
"""
from util import get_puzzle_input_lines, run_file, start_timer, get_elapsed_ms


def parse_input():
    [puzzle_input] = get_puzzle_input_lines('day09')
    data = []

    is_file = True
    file_id = 0
    for i in range(len(puzzle_input)):
        value = int(puzzle_input[i])
        for _ in range(value):
            if is_file:
                data.append(file_id)
            else:
                data.append(None)
        if is_file:
            file_id += 1

        is_file = not is_file
    return data

def print_data(data):
    data_string = ''
    for d in data:
        data_string += '.' if d is None else str(d)
    print(f'{data_string} ({len(data_string)})')

def part1():
    data = parse_input()

    free_index = 0
    move_index = len(data) - 1
    while data[move_index] is None:
        move_index -= 1


    while True:
        if data[free_index] is not None:
            free_index += 1
            continue

        if free_index >= move_index -1:
            break

        data[free_index] = data[move_index]
        data[move_index] = None
        move_index -= 1

    total = 0
    for i in range(len(data)):
        value = data[i]
        if value is not None:
            total += i * value
    return total



min_free_spot_by_length = {}
def find_free_spot(data, length, max_spot):
    global min_free_spot_by_length
    free_spot_start, free_spot_end = None, None
    start_looking = min_free_spot_by_length.get(length, 0)
    for i in range(start_looking, len(data)):
        if i > max_spot:
            break
        if data[i] is None:
            if free_spot_start is None:
                free_spot_start = i
            free_spot_end = i
            if free_spot_end - free_spot_start + 1 == length:
                min_free_spot_by_length[length] = free_spot_end + 1
                return free_spot_start, free_spot_end
        else:
            free_spot_start = None

    return None, None


def find_last_index(data, value, max_index_to_consider = None):
    if max_index_to_consider is None:
        max_index_to_consider = len(data) - 1
    return max_index_to_consider - data[:max_index_to_consider + 1][::-1].index(value)


def part2():
    data = parse_input()

    file_id = max(filter(lambda d: d is not None, data))
    move_index = find_last_index(data, file_id)


    while True:
        if file_id == 0:
            break

        start_move_index = move_index
        while data[start_move_index] == file_id:
            start_move_index -= 1
        start_move_index +=1

        move_length = move_index - start_move_index + 1
        free_spot_start, free_spot_end = find_free_spot(data, move_length, start_move_index-1)

        if free_spot_start is not None:
            for i in range(move_index - start_move_index + 1):
                data[free_spot_start + i] = data[start_move_index + i]
                data[start_move_index + i] = None

        move_index = start_move_index - 1
        while data[move_index] != file_id - 1:
            move_index = move_index - 1

        file_id -= 1

    total = 0
    for index, value in enumerate(data):
        if value is not None:
            total += index * value



    return total

run_file()
# Day 9:
# 	Part 1: 6448989155953  execution time: 15.2ms
# 	Part 2: 6476642796832  execution time: 35.2ms
