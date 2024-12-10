import os

def py_contents(day):
    return f"""\"\"\"
https://adventofcode.com/2024/day/{day}
\"\"\"
from util import get_input, run_file

def parse_input():
    lines = get_input('day{day}')
    return lines

def part1():
    answer = 0
    return answer
    
def part2():
    answer = 0
    return answer

run_file()
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