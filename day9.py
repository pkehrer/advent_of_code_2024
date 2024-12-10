"""
https://adventofcode.com/2024/day/19
"""
from util import get_input, time_fn

def parse_input():
    [puzzle_input] = get_input('day9')
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
    return data, file_id - 1

def print_data(data):
    data_string = ''
    for d in data:
        data_string += '.' if d is None else str(d)
    print(f'{data_string} ({len(data_string)})')

def part1():
    data, _ = parse_input()

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
    print(f'Part 1: {total}')

def find_free_spot(data, length, max_spot):
    free_spot_start, free_spot_end = None, None
    for i in range(len(data)):
        if i > max_spot:
            break
        if data[i] is None:
            if free_spot_start is None:
                free_spot_start = i
            free_spot_end = i
            if free_spot_end - free_spot_start + 1 == length:
                return free_spot_start, free_spot_end
        else:
            free_spot_start = None

    return None, None


def find_last_index(data, value):
    for i, data_value in enumerate(reversed(data)):
        if data_value == value:
            return len(data) - i - 1

def part2():
    data, max_file_id = parse_input()

    for file_id in reversed(range(max_file_id+1)):
        if file_id == 0:
            break

        move_index = find_last_index(data, file_id)
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
        while data[move_index] is None:
            move_index = move_index - 1

    total = 0
    for index, value in enumerate(data):
        if value is not None:
            total += index * value
    print(f'Part 2:{total}')


print('Day 9:')
time_fn(part1) # 6448989155953
time_fn(part2) # 6476642796832