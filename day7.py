from typing import DefaultDict


def part_one(data):
    crabs = {}
    for i in data:
        crabs[i] = 1 if i not in crabs else crabs[i]+1

    position_cost = {}

    r = max(crabs.keys())

    for i in range(r+1):
        if i not in position_cost: position_cost[i] = 0
        for k, v in crabs.items():
            position_cost[i] += abs(i - k) * v
    

    print(min(position_cost.values()))


def part_two(data):
    crabs = {}
    for i in data:
        crabs[i] = 1 if i not in crabs else crabs[i]+1

    position_cost = {}

    r = max(crabs.keys())

    for i in range(r+1):
        if i not in position_cost: position_cost[i] = 0
        for k, v in crabs.items():
            delta = abs(i - k)
            position_cost[i] += sum(range(delta+1)) * v
    

    print(min(position_cost.values()))


if __name__ == '__main__':
    data = list(map(int, open('input7_1.txt', 'r').read().split(',')))
    part_one(data[:])
    part_two(data[:])
