"""
https://adventofcode.com/2024/day/13
"""

from util import get_puzzle_input_lines

def parse_input(prize_offset = 0):
    def parse_line(btn_line, sep):
        x_expr, y_expr = btn_line.split(' ')[-2:]
        return int(x_expr.strip(',').split(sep)[1]), int(y_expr.split(sep)[1])

    lines = get_puzzle_input_lines('day13')
    games = []
    for line_start in range(0, len(lines), 4):
        a_btn_line, b_btn_line, prize_line = lines[line_start:line_start+3]
        prize = parse_line(prize_line, '=')

        games.append({
            'a_change': parse_line(a_btn_line, '+'),
            'b_change': parse_line(b_btn_line, '+'),
            'prize': (prize[0] + prize_offset, prize[1] + prize_offset)
        })
    return games

def round_if_int(number):
    epsilon = .00001
    rounded = round(number)
    return None if abs(number - rounded) > epsilon else rounded

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
    px, py = game['prize']
    ax, ay = game['a_change']
    bx, by = game['b_change']

    b_presses = round_if_int((py * ax - px * ay) / (ax * by - ay * bx))
    if b_presses is None:
        return 0

    a_presses = round_if_int((px - (bx * b_presses)) / ax)
    if a_presses is None:
        return 0

    return a_presses * 3 + b_presses


def part1():
    total = 0
    games = parse_input()
    for i, game in enumerate(games):
        cost = play_game(game)
        total += cost

    return total
    
def part2():
    total = 0
    games = parse_input(10000000000000)
    for i, game in enumerate(games):
        cost = play_game(game)
        total += cost

    return total

# Day 13 🎄
# 	Part 1: 28059             execution time: 1.0ms
# 	Part 2: 102255878088512   execution time: 1.0ms
