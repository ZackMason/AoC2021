from util import *
import numpy as np

def part_one_clean():
    data = parse_input()
    l = len(data[0])

    histo = [0 for i in range(l)]

    col = [[x for x in line] for line in data]
    
    col = [''.join(x) for x in np.transpose(col)]


    print(f'{col}')

def part_one():
    data = parse_input()
    cols = np.transpose([[c for c in line] for line in data])
    count = [sum([int(x) for x in col]) for col in cols]
    h = len(data) // 2
    print(int(''.join(['1' if x > h else '0' for x in count]),2)*int(''.join(['0' if x > h else '1' for x in count]),2))


def part_two():
    data = parse_input()
    i = 0
    ox = data[:]
    co2 = data[:]

    while len(ox) > 1:
        ones = [0,0,0,0,0,0,0,0,0,0,0,0]
        zeros = [0,0,0,0,0,0,0,0,0,0,0,0]

        for line in ox:
            if line[i] == '1':
                ones[i] += 1
            elif line[i] == '0':
                zeros[i] += 1

        most_common = '1' if ones[i] >= zeros[i] else '0'

        ox = [x for x in ox if x[i] == most_common]
        i+=1
    print(ox)

    i=0
    while len(co2) > 1:
        ones = [0,0,0,0,0,0,0,0,0,0,0,0]
        zeros = [0,0,0,0,0,0,0,0,0,0,0,0]

        for line in co2:
            if line[i] == '1':
                ones[i] += 1
            elif line[i] == '0':
                zeros[i] += 1

        most_common = '1' if ones[i] < zeros[i] else '0'

        co2 = [x for x in co2 if x[i] == most_common]
        i+=1
    print(co2)

    print(int(ox[0],base=2) * int(co2[0], base=2))


if __name__ == '__main__':
    part_one()