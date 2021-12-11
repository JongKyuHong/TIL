from collections import deque


def brute_force(arr, bottom, n):
    arr = deque(arr)
    result = 0
    maxa = 0
    for i in range(n):
        a,b,c,d,e,f = arr.popleft()
        if bottom == a: # A가 밑면에 있는 상황을 말함
            maxa = max(b,c,d,e)
            result += maxa
            bottom = f
        elif bottom == b:
            maxa = max(a,c,e,f)
            result += maxa
            bottom = d
        elif bottom == c:
            maxa = max(a,b,d,f)
            result += maxa
            bottom = e
        elif bottom == d:
            maxa = max(a,c,e,f)
            result += maxa
            bottom = b
        elif bottom == e:
            maxa = max(a,b,d,f)
            result += maxa
            bottom = c
        elif bottom == f:
            maxa = max(b,c,d,e)
            result += maxa
            bottom = a
    return result

n = int(input())
cubes = [list(map(int, input().split())) for _ in range(n)]
res = 0
for i in range(1,7):
    res = max(res,brute_force(cubes, i, n))
    # if i == 0:
    #     result += 5
    # elif i == 1:
    #     result += 3
    # elif i == 2:
    #     result += 4
    # elif i == 3:
    #     result += 3
    # elif i == 4:
    #     result += 2
    # else:
    #     result += 1
print(res)
# A0 : 5F
# B1 : 3D
# C2 : 4E
# D3 : 1B
# E4 : 2C
# F5 : A0

# 3 4 1 2 2







