from util import get_input, time_fn

def parse_input():
    rules = []
    sequences = []
    for line in get_input('day5'):
        if '|' in line:
            nums = line.split('|')
            rules.append((nums[0], nums[1]))
        elif ',' in line:
            nums = line.split(',')
            sequences.append(nums)

    return rules, sequences

def is_sequence_valid(sequence, rules):
    for letter_pos, letter in enumerate(sequence):
        for rule in [r for r in rules if r[0] == letter]:
            if rule[1] in sequence:
                next_letter_pos = sequence.index(rule[1])
                if next_letter_pos < letter_pos:
                    return False, rule
    return True, None

def swap(arr, rule):
    i1 = arr.index(rule[0])
    i2 = arr.index(rule[1])
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp

def part1():
    score = 0
    rules, sequences = parse_input()
    for sequence in sequences:
        valid, _  = is_sequence_valid(sequence, rules)
        if valid:
            middle_letter = sequence[int((len(sequence) - 1) / 2)]
            score += int(middle_letter)

    print(f'Part 1: {score}')

def part2():
    rules, sequences = parse_input()
    score = 0
    for sequence in sequences:
        valid, broken_rule = is_sequence_valid(sequence, rules)
        if valid:
            continue
        while not valid:
            swap(sequence, broken_rule)
            valid, broken_rule = is_sequence_valid(sequence, rules)
        middle_letter = sequence[int((len(sequence) -1) /2)]
        score += int(middle_letter)
    print(f'Part 2: {score}')

print('Day 5:')
time_fn(part1) # 4996
time_fn(part2) # 6311