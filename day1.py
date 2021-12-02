
def text_to_list():
    l = []
    try:
        while t:=input():
            l.append(t)
    except:
        return l


if __name__ == '__main__':
    data = text_to_list()
    windows = [data[i:i+3] for i in range(len(data)-2)]
    inc = 0
    for i in range(len(windows)-1):
        if sum(windows[i]) < sum(windows[i+1]):
            inc += 1
    print(f'Answer: {inc}')

def part_one(): 
    i = 0
    l = None

    try:
        while t:=int(input()):
            if l and t>l:
                i+=1
            l = t
    except:
        print(f'Answer: {i}')
    