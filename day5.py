def part_one(data):
    board = [[0 for y in range(1000)] for x in range(1000)]

    for line in data:
        x1, y1, x2, y2 = line

        dx = abs(x2 - x1) + 1
        dy = abs(y2 - y1) + 1

        if x1 == x2:
            for i in range(dy):
                board[x1][min(y1,y2)+i] += 1
        elif y1 == y2:
            for i in range(dx):
                board[min(x1,x2)+i][y1] += 1

    a = 0
    [[a := a + 1 for cell in row if cell >= 2] for row in board]
    print(f'{a=}')

def part_two(data):
    board = [[0 for y in range(1000)] for x in range(1000)]

    for line in data:
        x1, y1, x2, y2 = line

        dx = abs(x2 - x1) + 1
        dy = abs(y2 - y1) + 1

        if x1 == x2:
            for i in range(dy):
                board[x1][min(y1,y2)+i] += 1
        elif y1 == y2:
            for i in range(dx):
                board[min(x1,x2)+i][y1] += 1
        else:
            coeff = [1 if x1<x2 else -1, 1 if y1<y2 else -1]
            for i in range(dy):
                board[x1+i*coeff[0]][y1+i*coeff[1]] += 1


    a = 0
    [[a := a + 1 for cell in row if cell >= 2] for row in board]
    print(f'{a=}')


if __name__ == '__main__':
    data = [line.strip()  for line in open('input5_1.txt', 'r').readlines() if line.strip() != '']
    data = [line.replace('->', ',').split(',') for line in data]
    data = [list(map(int,line)) for line in data]
    part_one(data[:])
    part_two(data[:])
