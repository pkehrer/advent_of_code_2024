import util
from text_util import christmas_text, red_text, green_text


def run_file(filename):
    module_name = filename.replace('.py', '')
    day = int(module_name.split('day')[1])
    module = __import__(module_name)

    print(red_text('Day ') + green_text(f'{day} 🎄'))

    for num, part in [(1, getattr(module, 'part1', None)), (2,getattr(module, 'part2', None))]:
        if part is None:
            print(christmas_text(f'\tPart {num} not defined'))
        else:
            start = util.start_timer()
            answer = str(part())
            padding = ''
            for i in range(14 - len(answer)):
                padding = padding + ' '
            print(christmas_text(f'\tPart {num}: ') + answer + padding, end='')
            util.print_elapsed_time(start)
