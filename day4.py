from util import *
import numpy as np

def check_board(board, marked):
    check = [[1 if c in marked else 0 for c in row] for row in board]
    answer = sum([sum([int(c) if c not in marked else 0 for c in row]) for row in board])
    for row in check:
        if sum(row) == 5:
            return answer
    for col in np.transpose(check):
        if sum(col) == 5:
            return answer
    return False

def part_one(data):
    cmds, *boards = data

    cmds = cmds.split(',')

    boards = [np.array([y.split() for y in boards][x:x+5:]) for x in range(0, len(boards), 5)]
    
    marked, *cmds = cmds
    marked = [marked]

    while len(cmds) > 0:
        marked.append(cmds.pop(0))
        for b in boards:
            if (a := check_board(b, marked)) != False:
                print('Answer: ', a * int(marked[-1]) )
                return

def part_two(data):
    cmds, *boards = data

    cmds = cmds.split(',')

    boards = [np.array([y.split() for y in boards][x:x+5:]) for x in range(0, len(boards), 5)]
    
    marked, *cmds = cmds
    marked = [marked]

    last_a = None

    while len(cmds) > 0:
        marked.append(cmds.pop(0))
        for b in boards:
            if (a := check_board(b, marked)) != False:
                last_a = a * int(marked[-1])
        boards = [b for b in boards if not (check_board(b, marked))]
    
    print('Answer: ', last_a )

if __name__ == '__main__':
    data = parse_input()

    data = [x for x in data if x != '']

    part_one(data[:])
    part_two(data[:])
