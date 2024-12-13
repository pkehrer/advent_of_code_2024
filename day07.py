"""
https://adventofcode.com/2024/day/7
"""
from util import get_puzzle_input_lines


def parse_input():
    lines = get_puzzle_input_lines('day07')
    records = []
    for line in lines:
        [result, numbers_str] = line.split(': ')
        numbers = [int(n) for n in numbers_str.split(' ')]
        records.append((int(result), numbers))
    return records


def get_result(current_result: int, desired_result: int, numbers: list[int], index=0, include_pipe=False):
    if index == len(numbers):
        return current_result if current_result == desired_result else 0

    plus_result = get_result(current_result + numbers[index], desired_result, numbers, index + 1, include_pipe)
    if plus_result > 0:
        return plus_result

    mult_result = get_result(current_result * numbers[index], desired_result, numbers, index + 1, include_pipe)
    if mult_result > 0:
        return mult_result

    if include_pipe:
        result_of_pipe_operator = int(str(current_result) + str(numbers[index]))
        pipe_results = get_result(result_of_pipe_operator, desired_result, numbers, index + 1, include_pipe)
        if pipe_results > 0:
            return pipe_results

    return 0


def part1():
    records = parse_input()
    score = 0

    for record in records:
        record_score = get_result(current_result=record[1][0],
                                  desired_result=record[0],
                                  numbers=record[1][1:])

        score += record_score

    return score


def part2():
    records = parse_input()
    score = 0

    for record in records:
        record_score = get_result(current_result=record[1][0],
                                  desired_result=record[0],
                                  numbers=record[1][1:],
                                  index=0,
                                  include_pipe=True)

        score += record_score

    return score

# Day 7 👼
# 	Part 1: 66343330034722    execution time: 44.9ms
# 	Part 2: 637696070419031   execution time: 1602.3ms
