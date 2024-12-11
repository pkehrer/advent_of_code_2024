import time
from text_util import italic_text, green, green_text, christmas_text


def get_puzzle_input_lines(filename):
    with (open(f'input/{filename}.txt', 'r') as f):
        return [l.rstrip('\n') for l in f.readlines()]

def start_timer():
    return time.perf_counter()

def get_elapsed_ms(start):
    end = time.perf_counter()
    seconds = end - start
    return seconds * 1000

def print_elapsed_time(start):
    end = time.perf_counter()
    seconds = end - start
    time_string = f'{(seconds * 1000):.1f}ms'
    print(italic_text(christmas_text('  execution time: ') + green_text(time_string)))

