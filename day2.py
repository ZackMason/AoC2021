from util import *

def part_one():
    data = parse_input()

    pos = [0, 0]
    for cmd in data:
        match [c:=cmd.split(), c[0], int(c[1])]:
            case [_, 'forward', i]:
                pos[0] += i
            case [_, 'down', i]:
                pos[1] += i
            case [_, 'up', i]:
                pos[1] -= i
            case _:
                print('Unknown cmd')

    print(f'{pos=}, Answer: ', end='')
    print(pos[0]*pos[1])

def part_two():
    data = parse_input()

    pos = [0, 0, 0]
    for cmd in data:
        match [c:=cmd.split(), c[0], int(c[1])]:
            case [_, 'forward', i]:
                pos[0] += i
                pos[1] += pos[2] * i
            case [_, 'down', i]:
                pos[2] += i
            case [_, 'up', i]:
                pos[2] -= i
            case _:
                print('Unknown cmd')

    print(f'{pos=}, Answer: ', end='')
    print(pos[0]*pos[1])

if __name__ == '__main__':
    part_two()