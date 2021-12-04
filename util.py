
def text_to_list():
    l = []
    try:
        while t:=input():
            l.append(t)
    except:
        return l

def parse_input():
    l = []
    try:
        while True:
            l.append(input())
        return [x for x in l if x != '']
    except:
        return [x for x in l if x != '']
