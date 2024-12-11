from text_util import christmas_text, green_text
from util import start_timer, get_elapsed_ms
from os import listdir
from re import search
from runner import run_file
from create_files import default_day_py_contents

files = [f for f in listdir('.') if search(r"day\d+\.py", f) is not None]
files.sort()
files = [f for f in files if open(f, 'r').read() != default_day_py_contents(int(f.split('day')[1].split('.')[0]))]

start = start_timer()

for f in files:
    run_file(f)

ms = get_elapsed_ms(start)
time_string = f'{(ms / 1000):.2f}s'
print(christmas_text('\nTotal execution time: ') + green_text(time_string))
