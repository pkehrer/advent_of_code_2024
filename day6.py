from util import get_input, time_fn

def parse_input():
    lines = get_input('day6')
    return [[cell for cell in list(l)] for l in lines]

def find_guard(map):
    for y, row in enumerate(map):
        if '^' in row:
            return row.index('^'), y


def turn90(direction):
    if direction == 'up':
        return 'right'
    if direction == 'right':
        return 'down'
    if direction == 'down':
        return 'left'
    if direction == 'left':
        return 'up'

def next_step(x, y, direction):
    if direction == 'up':
        return x, y-1
    if direction == 'right':
        return x+1, y
    if direction == 'down':
        return x, y+1
    if direction == 'left':
        return x-1, y
    raise RuntimeError("this shouldn't happen")

def walk_map(the_map):
    x, y = find_guard(the_map)
    the_map[y][x] = 'X'
    direction = 'up'
    while True:
        nextx, nexty = next_step(x, y, direction)
        if nextx < 0 or nextx >= len(the_map[0]) or nexty < 0 or nexty >= len(the_map):
            break

        next_spot = the_map[nexty][nextx]

        if next_spot == '#':
            direction = turn90(direction)
        else:
            the_map[nexty][nextx] = 'X'
            x = nextx
            y = nexty

def part1():
    the_map = parse_input()
    walk_map(the_map)
    score = 0 # one spot for his starting position?
    for row in the_map:
        score += len([cell for cell in row if cell == 'X'])
    print(f'Part 1: {score}')


def map_has_loop(the_map):
    x, y = find_guard(the_map)
    the_map[y][x] = 'X'
    direction = 'up'

    while True:
        nextx, nexty = next_step(x,y, direction)

        if nextx < 0 or nextx >= len(the_map[0]) or nexty < 0 or nexty >= len(the_map):
            return False

        next_spot = the_map[nexty][nextx]

        if next_spot == '#':
            direction = turn90(direction)
        else:
            x = nextx
            y = nexty
            if next_spot == direction:
                return True
            else:
                the_map[nexty][nextx] = direction


def part2():
    a_map = parse_input()
    guard_x, guard_y = find_guard(a_map)
    walk_map(a_map)
    possible_blocker_positions = []

    for y, row in enumerate(a_map):
        for x, cell in enumerate(row):
            if a_map[y][x] == 'X' and not (guard_x == x and guard_y == y):
                possible_blocker_positions.append((x, y))

    good_spots = 0
    for blocker_x, blocker_y in possible_blocker_positions:
        the_map = parse_input()
        the_map[blocker_y][blocker_x] = '#'
        if map_has_loop(the_map):
            good_spots += 1

    print(f'Part 2: {good_spots}')

print('Day 6:')
time_fn(part1) # 5153
time_fn(part2) # 1711