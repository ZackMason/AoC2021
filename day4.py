import numpy as np

def check_board(board, marked):
    check = [[c if c not in marked else 0 for c in row] for row in board]
    bool_array = ~np.array(check, dtype=bool)
    if True in [*np.all(bool_array, axis=0), *np.all(bool_array.T, axis=0)]:
        return marked[-1] * np.sum(check)
    return False

def solve(data):
    cmds, *boards = data
    
    cmds = list(map(int, cmds.split(',')))
    boards = [np.array([ list(map(int, y.split())) for y in boards[x:x+5:]]) for x in range(0, len(boards), 5)]
    
    last_a = None

    def f(b, marked):
        nonlocal last_a 
        if a := check_board(b, marked):
            if last_a == None:
                print('Answer: ', a )
            last_a = a
            return False
        return True

    for i in range(len(cmds)):
        boards = [b for b in boards if f(b, cmds[0:i+1])]
        if len(boards) == 0: break

    print('Answer: ', last_a )

if __name__ == '__main__':
    data = [line.strip() for line in open('input4_1.txt', 'r').readlines() if line.strip() != '']
    solve(data[:])
