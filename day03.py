"""
https://adventofcode.com/2024/day/3
"""
import re

from util import get_puzzle_input_lines


def parse_input():
    return get_puzzle_input_lines('day03')

def part1():
    total = 0
    for line in parse_input():
        pattern = r"mul\(\d+,\d+\)"
        match = re.findall(pattern, line)
        for expr in match:
            nums = list(map(lambda s: int(s), re.findall(r'\d+', expr)))
            product = nums[0] * nums[1]
            total += product

    return total


def part2():
    small_total = 0
    enabled = True

    for line in parse_input():
        pattern = r"(mul\(\d+,\d+\)|do\(\)|don\'t\(\))"
        match = re.findall(pattern, line)

        for expr in match:
            if expr == 'do()':
                enabled = True
            elif expr == 'don\'t()':
                enabled = False
            elif enabled:
                nums = list(map(lambda s: int(s), re.findall(r'\d+', expr)))
                product = nums[0] * nums[1]
                small_total += product

    return small_total

# Day 3:
# 	Part 1: 191183308  execution time: 1.0ms
# 	Part 2: 92082041  execution time: 0.6ms
