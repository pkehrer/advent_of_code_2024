"""
https://adventofcode.com/2024/day/7
"""
from util import get_puzzle_input_lines, run_file


def parse_input():
    lines = get_puzzle_input_lines('day07')
    records = []
    for line in lines:
        [result, numbers_str] = line.split(': ')
        numbers = [int(n) for n in numbers_str.split(' ')]
        records.append((int(result), numbers))
    return records


def get_possible_results(current_result, remaining_numbers):
    if len(remaining_numbers) == 1:
        return [current_result + remaining_numbers[0], current_result * remaining_numbers[0]]

    plus_results = get_possible_results(current_result + remaining_numbers[0], remaining_numbers[1:])
    mult_results = get_possible_results(current_result * remaining_numbers[0], remaining_numbers[1:])

    return plus_results + mult_results

def get_possible_results_with_pipe(current_result, numbers, index):
    if index == len(numbers):
        return [current_result]

    plus_results = get_possible_results_with_pipe(
        current_result + numbers[index],
        numbers,
        index+1)
    mult_results = get_possible_results_with_pipe(
        current_result * numbers[index],
        numbers,
        index+1)
    pipe_results = get_possible_results_with_pipe(
        int(str(current_result) + str(numbers[index])),
        numbers,
        index+1)

    return plus_results + mult_results + pipe_results

def part1():
    records = parse_input()
    score = 0

    for record in records:
        possible_results = get_possible_results(record[1][0], record[1][1:])
        if record[0] in possible_results:
            score += record[0]

    return score

def part2():
    records = parse_input()
    score = 0

    for record in records:
        possible_results = get_possible_results_with_pipe(record[1][0], record[1], 1)
        if record[0] in possible_results:
            score += record[0]

    return score

run_file()
# Day 7:
# 	Part 1: 66343330034722  execution time: 44.2ms
# 	Part 2: 637696070419031  execution time: 4635.0ms
