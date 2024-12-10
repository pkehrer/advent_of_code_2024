import os

def py_contents(day):
    return f"""from util import get_input, time_fn

def parse_input():
    lines = get_input('day{day}')
    return lines

def part1():
    answer = 0
    print(f'Part 1: {{answer}}') 
    
def part2():
    answer = 0
    print(f'Part 2: {{answer}}')

print('Day {day}:')
time_fn(part1) #
time_fn(part2) #
"""

for i in range(1, 26):
    py_filename = f'day{i}.py'
    txt_filename = f'input/day{i}.txt'

    if not os.path.exists(py_filename):
        with open(py_filename, 'w') as file:
            file.write(py_contents(i))

    if not os.path.exists(txt_filename):
        with open(txt_filename, 'w') as file:
            file.write('')