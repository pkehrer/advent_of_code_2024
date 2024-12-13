"""
https://adventofcode.com/2024/day/13
"""

from util import get_puzzle_input_lines
import re


def parse_input(prize_offset=0):
    """
    store all relevant parameters from each game as tuple (ax, ay, bx, by, px, py).

    The following puzzle input would be represented as (94, 34, 22, 67, 8400, 5400)
    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400

    :param prize_offset: add this value to px and py for part2
    :return: as lit of the above tuples, one for each game
    """

    regex = r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)'
    lines = get_puzzle_input_lines('day13')
    games = []
    for line_start in range(0, len(lines), 4):
        game_text = '\n'.join(lines[line_start:line_start + 3])
        game = [int(x) for x in re.match(regex, game_text).groups()]
        game[-1], game[-2] = game[-1] + prize_offset, game[-2] + prize_offset
        games.append(game)
    return games


def play_game(game):
    """
    The solution to the game can be expressed as two equations:
      1.  (number of A presses) * (a button distance_x) + (numbmer of B presses) * (b button distance_x) = Prize_x
      2.  (number of A presses) * (a button distance_y) + (numbmer of B presses) * (b button distance_y) = Prize_y

    Using algebra, we can solve for number of B presses, and then for number of A presses (or the other way around, but hey):
        1. b_presses = (prize_y * abutton_x - prize_x * abutton_y) / (abutton_x * bbutton_y - abutton_y * bbutton_x)
        2. a_presses = (prize_x - bbutton_x * b_presses) / abutton_x

    When solutions to b_presses or a_presses are fractional, it suggests an unsolvable game (it would require part of
    a press of the button to get the solution).
    """
    ax, ay, bx, by, px, py = game

    b_presses = (py * ax - px * ay) / (ax * by - ay * bx)
    if not b_presses.is_integer():
        return 0

    a_presses = (px - (bx * b_presses)) / ax
    if not a_presses.is_integer():
        return 0

    return int(a_presses * 3 + b_presses)


def part1():
    costs = [play_game(game) for game in parse_input()]
    return sum(costs)


def part2():
    costs = [play_game(game) for game in parse_input(prize_offset=10000000000000)]
    return sum(costs)

# Day 13 🎄
# 	Part 1: 28059             execution time: 1.0ms
# 	Part 2: 102255878088512   execution time: 1.0ms
