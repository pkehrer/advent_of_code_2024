import time
import inspect
import re

def get_puzzle_input_lines(filename):
    with (open(f'input/{filename}.txt', 'r') as f):
        return [l.rstrip('\n') for l in f.readlines()]

def start_timer():
    return time.perf_counter()

def get_elapsed_ms(start):
    end = time.perf_counter()
    seconds = end - start
    return seconds * 1000

def time_fn(fn):
    start = time.perf_counter()
    fn()
    end = time.perf_counter()
    seconds = end - start
    time_string = f'{(seconds * 1000):.1f}ms'
    print(f'\x1B[3m  execution time: {time_string}\x1B[23m')

def print_elapsed_time(start):
    end = time.perf_counter()
    seconds = end - start
    time_string = f'{(seconds * 1000):.1f}ms'
    print(f'\x1B[3m  execution time: {time_string}\x1B[23m')

def run_file():
    caller_index = -1
    stack = inspect.stack()
    caller = stack[caller_index]

    while re.search(r"\/day\d+\.py", caller.filename) is None:
        caller_index -= 1
        caller = stack[caller_index]

    day_number = caller.filename.split('/day')[1].split('.')[0]

    print(f'Day {day_number}:')

    part1_function = caller.frame.f_locals.get('part1')
    part2_function = caller.frame.f_locals.get('part2')

    if part1_function is None:
        print('\tPart 1 not defined')
    else:
        start = time.perf_counter()
        print(f'\tPart 1: {part1_function()}', end='')
        print_elapsed_time(start)

    if part2_function is None:
        print('\tPart 2 not defined')
    else:
        start = time.perf_counter()
        print(f'\tPart 2: {part2_function()}', end='')
        print_elapsed_time(start)
