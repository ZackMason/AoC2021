from util import *

def part_one():
    data = parse_input()

    pos = [0, 0]
    for cmd in data:
        match cmd.split():
            case ['forward', i]:
                pos[0] += int(i)
            case ['down', i]:
                pos[1] += int(i)
            case ['up', i]:
                pos[1] -= int(i)
            case _:
                print('Unknown cmd')

    print(f'{pos=}, Answer: ', end='')
    print(pos[0]*pos[1])

def part_two():
    data = parse_input()

    pos = [0, 0, 0]
    for cmd in data:
        match cmd.split():
            case ['forward', i]:
                pos[0] += int(i)
                pos[1] += pos[2] * int(i)
            case ['down', i]:
                pos[2] += int(i)
            case ['up', i]:
                pos[2] -= int(i)
            case _:
                print('Unknown cmd')

    print(f'{pos=}, Answer: ', end='')
    print(pos[0]*pos[1])

if __name__ == '__main__':
    part_two()