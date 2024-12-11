import os

def default_day_py_contents(day):
    return f"""\"\"\"
https://adventofcode.com/2024/day/{day}
\"\"\"
from util import get_puzzle_input_lines

def parse_input():
    lines = get_puzzle_input_lines('day{day:02}')
    return lines

def part1():
    answer = 0
    return answer
    
def part2():
    answer = 0
    return answer

"""

for i in range(1, 26):
    py_filename = f'day{i:02}.py'
    txt_filename = f'input/day{i:02}.txt'

    if not os.path.exists(py_filename):
        with open(py_filename, 'w') as file:
            file.write(default_day_py_contents(i))

    if not os.path.exists(txt_filename):
        with open(txt_filename, 'w') as file:
            file.write('')