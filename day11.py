"""
https://adventofcode.com/2024/day/11
"""
from util import get_puzzle_input_lines, increment_dict


# returns stones as a dictionary of stones to counts, where the counts are the count of that stone type in the line.
def parse_input():
    stones = get_puzzle_input_lines('day11')[0].split(' ')
    counts = {}
    for stone in stones:
        if stone not in counts:
            counts[stone] = 1
        else:
            counts[stone] += 1
    return counts

def blink_at_stones(stone_counts):
    new_stone_counts = {}
    for stone, count in stone_counts.items():
        if stone == '0':
            increment_dict(new_stone_counts, '1', count)
        elif len(stone) % 2 == 0:
            half_index = int(len(stone) / 2)
            increment_dict(new_stone_counts, stone[:half_index], count)
            increment_dict(new_stone_counts, str(int(stone[half_index:])), count)
        else:
            increment_dict(new_stone_counts, str(int(stone) * 2024), count)
    return new_stone_counts

part1_stone_counts = {}

def part1():
    global part1_stone_counts
    stone_counts = parse_input()
    for i in range(25):
        stone_counts = blink_at_stones(stone_counts)

    part1_stone_counts = stone_counts
    return sum(stone_counts.values())

def part2():
    global part1_stone_counts
    stone_counts = {k:v for (k,v) in part1_stone_counts.items()}
    for i in range(50):
        stone_counts = blink_at_stones(stone_counts)

    return sum(stone_counts.values())

# Day 11 🎄
# 	Part 1: 199946            execution time: 1.4ms
# 	Part 2: 237994815702032   execution time: 52.9ms
