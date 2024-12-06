from util import get_input, time_fn


def parse_input():
    lines = get_input('day2')
    return [[int(cell) for cell in line.split()] for line in lines]

def is_safe(report):
    increasing = report[1] > report[0]
    prev_val = report[0]
    for val in report[1:]:
        diff = abs(val - prev_val)
        if diff < 1 or diff > 3:
            return False
        if (val > prev_val) != increasing:
            return False

        prev_val = val
    return True

def is_safe_dampened(report):
    for i in range(len(report)):
        edited_report = list(report)
        edited_report.pop(i)
        if is_safe(edited_report):
            return True
    return False

def part1():
    safe_reports = 0
    for report in parse_input():
        if is_safe(report):
            safe_reports += 1

    print(f'Part 1: {safe_reports}')

def part2():
    safe_dampened_reports = 0
    for report in parse_input():
        if is_safe_dampened(report):
            safe_dampened_reports += 1

    print(f'Part 2: {safe_dampened_reports}')

print('Day 2:')
time_fn(part1) # 639
time_fn(part2) # 674