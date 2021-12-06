def solve(data, p2 = False):
    board = {}

    for line in data:
        x1, y1, x2, y2 = line

        dx = abs(x2 - x1) + 1
        dy = abs(y2 - y1) + 1
        dir = [0 if x1==x2 else 1 if x1<x2 else -1, 0 if y1==y2 else 1 if y1<y2 else -1]

        if not p2 and 0 not in dir:
            continue

        for i in range(max(dx,dy)):
            pos = '%d %d' % (x1+i*dir[0], y1+i*dir[1])
            if pos not in board: board[pos] = 0
            board[pos] += 1

    a = 0
    [a := a + 1 for count in board.values() if count >= 2] 
    print(f'{a=}')

if __name__ == '__main__':
    data = [(*map(int, line.replace('->', ',').split(',')),)  for line in open('input5_1.txt', 'r')]
    solve(data[:])
    solve(data[:], True)
