from util import start_timer, print_elapsed_time, get_elapsed_ms

start = start_timer()

import day01
import day02
import day03
import day04
import day05
import day06
import day07
import day08
import day09
import day10
# import day11
# import day12
# import day13
# import day14
# import day15
# import day16
# import day17
# import day18
# import day19
# import day20
# import day21
# import day22
# import day23
# import day24
# import day25

ms = get_elapsed_ms(start)
time_string = f'{(ms / 1000):.2f}s'
print(f'\n\x1B[3m  Total execution time: {time_string}\x1B[23m')