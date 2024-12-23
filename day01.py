"""
https://adventofcode.com/2024/day/1
"""
from util import get_puzzle_input_lines


def parse_input():
    list1 = []
    list2 = []
    for line in get_puzzle_input_lines('day01'):
        tokens = line.split()
        list1.append(tokens[0])
        list2.append(tokens[1])
    return list1, list2

def get_list_ranks(a_list):
    sorted_list = list(a_list)
    sorted_list.sort()
    list_with_ranks = []
    for num in a_list:
        rank = sorted_list.index(num)
        sorted_list[rank] = None
        list_with_ranks.append([num, rank + 1])
    return list_with_ranks

def part1():
    list1, list2 = parse_input()
    ranks1 = get_list_ranks(list1)
    ranks2 = get_list_ranks(list2)

    list_distance = 0
    for i in range(len(list1)):
        rank1 = next(filter(lambda e: e[1] == i+1, ranks1))
        rank2 = next(filter(lambda e: e[1] == i+1, ranks2))

        list_distance += abs(int(rank1[0]) - (int(rank2[0])))

    return list_distance

def part2():
    list1, list2 = parse_input()
    similarity = 0
    for item1 in list1:
        items_in_2 = list(filter(lambda i: i == item1, list2))
        similarity += int(item1) * len(items_in_2)

    return similarity

# Day 1:
# 	Part 1: 2378066  execution time: 53.5ms
# 	Part 2: 18934359  execution time: 29.8ms
