"""
https://adventofcode.com/2024/day/5
"""
from util import get_puzzle_input_lines, run_file


def parse_input():
    rules = {}
    sequences = []
    for line in get_puzzle_input_lines('day05'):
        if '|' in line:
            nums = line.split('|')
            if nums[0] not in rules:
                rules[nums[0]] = []
            rules[nums[0]].append(nums[1])
        elif ',' in line:
            nums = line.split(',')
            sequences.append(nums)

    return rules, sequences

def is_sequence_valid(sequence, rules):
    for letter_pos, letter in enumerate(sequence):
        for must_be_after in rules[letter]:
            if must_be_after in sequence:
                next_letter_pos = sequence.index(must_be_after)
                if next_letter_pos < letter_pos:
                    return False, (letter_pos, next_letter_pos)
    return True, None

def part1():
    score = 0
    rules, sequences = parse_input()
    for sequence in sequences:
        valid, _  = is_sequence_valid(sequence, rules)
        if valid:
            middle_letter = sequence[int((len(sequence) - 1) / 2)]
            score += int(middle_letter)

    return score

def swap(arr, index_pair):
    i1, i2 = index_pair
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp

def part2():
    rules, sequences = parse_input()
    score = 0
    for sequence in sequences:
        valid, broken_rule = is_sequence_valid(sequence, rules)
        if valid: # skip "already valid" sequences
            continue

        while not valid:
            swap(sequence, broken_rule)
            valid, broken_rule = is_sequence_valid(sequence, rules)
        middle_letter = sequence[int((len(sequence) -1) /2)]
        score += int(middle_letter)
    return score

run_file()
# Day 5:
# 	Part 1: 4996  execution time: 8.5ms
# 	Part 2: 6311  execution time: 301.1ms
