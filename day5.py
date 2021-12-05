def solve(data, p2 = False):
    board = {}

    for line in data:
        x1, y1, x2, y2 = line

        dx = abs(x2 - x1) + 1
        dy = abs(y2 - y1) + 1
        coeff = [0 if x1==x2 else 1 if x1<x2 else -1, 0 if y1==y2 else 1 if y1<y2 else -1]

        if not p2 and 0 not in coeff:
            continue

        for i in range(max(dx,dy)):
            index = '%d %d' % (x1+i*coeff[0], y1+i*coeff[1])
            if index not in board: board[index] = 0
            board[index] += 1

    a = 0
    [a := a + 1 for _, count in board.items() if count >= 2] 
    print(f'{a=}')


if __name__ == '__main__':
    data = [line.strip()  for line in open('input5_1.txt', 'r').readlines() if line.strip() != '']
    data = [line.replace('->', ',').split(',') for line in data]
    data = [list(map(int,line)) for line in data]
    solve(data[:])
    solve(data[:], True)
