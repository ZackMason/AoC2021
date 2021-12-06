import numpy as np
from numpy.linalg import matrix_power

def solve(data, days = 81):
    fishes = {i:0 for i in range(-1, 9)}
    for d in data:
        fishes[d] += 1

    for day in range(1,days):
        next_fishes = {k - 1: v  for k, v in fishes.items()}
        for i in range(0, 8):
            fishes[i] = next_fishes[i]
        fishes[8] = next_fishes[-1]
        fishes[6] += next_fishes[-1]

    a = 0
    [a := a + v for v in fishes.values()]
    print(a)

# A**n * x = y
# x[0] + x[7] -> y[6]
# x[0] -> y[8]
def linalg_solution(data, days= 81):
    fishes = np.array([0 for i in range(9)])
    for i in data:
        fishes[i] += 1

    A = matrix_power(np.array([
    #   [0 1 2 3 4 5 6 7 8]
        [0,1,0,0,0,0,0,0,0], #[0]
        [0,0,1,0,0,0,0,0,0], #[1]
        [0,0,0,1,0,0,0,0,0], #[2]
        [0,0,0,0,1,0,0,0,0], #[3]
        [0,0,0,0,0,1,0,0,0], #[4]
        [0,0,0,0,0,0,1,0,0], #[5]
        [1,0,0,0,0,0,0,1,0], #[6]
        [0,0,0,0,0,0,0,0,1], #[7]
        [1,0,0,0,0,0,0,0,0], #[8]
    ], dtype=np.longlong), days)

    fishes =  A * fishes

    print(fishes.sum())

if __name__ == '__main__':
    data = list(map(int, open('input6_1.txt', 'r').read().split(',')))
    linalg_solution(data, days = 80)
    linalg_solution(data, days = 256)
    #solve(data[:])
    #solve(data[:], days=257)
