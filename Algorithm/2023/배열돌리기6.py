import sys
input = sys.stdin.readline

def updown_reverse(a, b, c, d):
    tmp = []
    for i in range(b-1, a-1, -1):
        t = []
        for j in range(c, d):
            t.append(lst[i][j])
        tmp.append(t)
    for i in range(a, b):
        for j in range(c, d):
            lst[i][j] = tmp[i-a][j-c]
    
def leftright_reverse(a, b, c, d):
    tmp = []
    for i in range(a, b):
        t = []
        for j in range(d-1, c-1, -1):
            t.append(lst[i][j])
        tmp.append(t)

    for i in range(a, b):
        for j in range(c, d):
            lst[i][j] = tmp[i-a][j-c]

def rightside_90(a, b, c, d):
    tmp = []
    for j in range(c, d):
        t = []
        for i in range(b-1, a-1, -1):
            t.append(lst[i][j])
        tmp.append(t)
    for i in range(a, b):
        for j in range(c, d):
            lst[i][j] = tmp[i-a][j-c]

def leftside_90(a, b, c, d):
    tmp = []
    for j in range(d-1, c-1, -1):
        t = []
        for i in range(a, b):    
            t.append(lst[i][j])
        tmp.append(t)
    for i in range(a, b):
        for j in range(c, d):
            lst[i][j] = tmp[i-a][j-c]

N, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(2**N)]
for _ in range(R):
    k, l = map(int, input().split())
    if k == 1:
        for i in range(0, 2**N, 2**l):
            for j in range(0, 2**N, 2**l):
                updown_reverse(i, i+2**l, j, j+2**l)
    elif k == 2:
        for i in range(0, 2**N, 2**l):
            for j in range(0, 2**N, 2**l):
                leftright_reverse(i, i+2**l, j, j+2**l)
    elif k == 3:
        for i in range(0, 2**N, 2**l):
            for j in range(0, 2**N, 2**l):
                rightside_90(i, i+2**l, j, j+2**l)
    elif k == 4:
        for i in range(0, 2**N, 2**l):
            for j in range(0, 2**N, 2**l):
                leftside_90(i, i+2**l, j, j+2**l)
    elif k == 5:
        updown_reverse(0, 2**N, 0, 2**N)
        for i in range(0, 2**N, 2**l):
            for j in range(0, 2**N, 2**l):
                updown_reverse(i, i+2**l, j, j+2**l)
    elif k == 6:
        leftright_reverse(0, 2**N, 0, 2**N)
        for i in range(0, 2**N, 2**l):
            for j in range(0, 2**N, 2**l):
                leftright_reverse(i, i+2**l, j, j+2**l)
    elif k == 7:
        rightside_90(0, 2**N, 0, 2**N)
        for i in range(0, 2**N, 2**l):
            for j in range(0, 2**N, 2**l):
                leftside_90(i, i+2**l, j, j+2**l)
    elif k == 8:
        leftside_90(0, 2**N, 0, 2**N)
        for i in range(0, 2**N, 2**l):
            for j in range(0, 2**N, 2**l):
                rightside_90(i, i+2**l, j, j+2**l)

for i in lst:
    print(*i)