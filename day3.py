"""
https://adventofcode.com/2024/day/3
"""
from util import get_input, time_fn
import re


def part1():
    total = 0
    for line in get_input('day3'):
        pattern = r"mul\(\d+,\d+\)"
        match = re.findall(pattern, line)
        for expr in match:
            nums = list(map(lambda s: int(s), re.findall(r'\d+', expr)))
            product = nums[0] * nums[1]
            total += product

    print(f'Part 1: {total}')


def part2():
    small_total = 0
    enabled = True

    for line in get_input('day3'):
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

    print(f'Part 2: {small_total}')

print('Day 3:')
time_fn(part1) # 191183308
time_fn(part2) # 92082041
