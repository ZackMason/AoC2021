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

if __name__ == '__main__':
    data = list(map(int, open('input6_1.txt', 'r').read().split(',')))
    solve(data[:])
    solve(data[:], days=257)
