from util import *
import numpy as np

def check_board(board, marked):
    check = [[c if c not in marked else 0 for c in row] for row in board]
    if True in [*np.all(~np.array(check, dtype=bool), axis=0), 
        *np.all(np.transpose(~np.array(check, dtype=bool)), axis=0)]:
            return marked[-1] * np.sum(check)
    return False

def part_one(data):
    cmds, *boards = data

    cmds = list(map(int, cmds.split(',')))

    boards = [np.array([ list(map(int, y.split())) for y in boards[x:x+5:]]) for x in range(0, len(boards), 5)]

    marked = [cmds.pop(0)]

    while len(cmds) > 0:
        marked.append(cmds.pop(0))
        for b in boards:
            if (a := check_board(b, marked)) != False:
                print('Answer: ', a)
                return

def part_two(data):
    cmds, *boards = data
    
    cmds = list(map(int, cmds.split(',')))
    boards = [np.array([ list(map(int, y.split())) for y in boards[x:x+5:]]) for x in range(0, len(boards), 5)]
    
    marked = [cmds.pop(0)]

    last_a = None

    def f(b, marked):
        nonlocal last_a 
        if a := check_board(b, marked):
            last_a = a
            return False
        return True

    while len(cmds) > 0 and len(boards) > 0:
        marked.append(cmds.pop(0))
        boards = [b for b in boards if f(b, marked)]

    print('Answer: ', last_a )

if __name__ == '__main__':
    data = parse_input()

    part_one(data[:])
    part_two(data[:])
