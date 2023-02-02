import sys
input = sys.stdin.readline

def updown(arr):
    lst = []
    for i in range(N-1, -1, -1):
        lst.append(arr[i])
    return lst

def leftright(arr):
    lst = []
    for i in range(N):
        tmp = []
        for j in range(M-1, -1, -1):
            tmp.append(arr[i][j])
        lst.append(tmp)
    return lst

def rotate_right(arr):
    lst = []
    for i in range(M):
        tmp = []
        for j in range(N-1,-1,-1):
            tmp.append(arr[j][i])
        lst.append(tmp)
    return lst

def rotate_left(arr):
    lst = []
    for i in range(M-1,-1,-1):
        tmp = []
        for j in range(N):
            tmp.append(arr[j][i])
        lst.append(tmp)
    return lst

def divide(n1,n2,m1,m2,arr):
    lst = []
    for i in range(n1, n2):
        tmp = []
        for j in range(m1, m2):
            tmp.append(arr[i][j])
        lst.append(tmp)
    return lst

def divide_rotate(arr, s):
    lst = []
    sector1 = divide(0, N//2, 0, M//2, arr)
    sector2 = divide(0, N//2, M//2, M, arr)
    sector4 = divide(N//2, N, 0, M//2, arr)
    sector3 = divide(N//2, N, M//2, M, arr)

    if s == 1:
        for i in range(N//2):
            idx = 0
            tmp = []
            while idx < M//2:
                tmp.append(sector4[i][idx])
                idx += 1
            idx = 0
            while idx < M//2:
                tmp.append(sector1[i][idx])
                idx += 1
            lst.append(tmp)
        
        for i in range(N//2):
            idx = 0
            tmp = []
            while idx < M//2:
                tmp.append(sector3[i][idx])
                idx += 1
            idx = 0
            while idx < M//2:
                tmp.append(sector2[i][idx])    
                idx += 1
            lst.append(tmp)
        return lst
    elif s == 2:
        for i in range(N//2):
            idx = 0
            tmp = []
            while idx < M//2:
                tmp.append(sector2[i][idx])
                idx += 1
            idx = 0
            while idx < M//2:
                tmp.append(sector3[i][idx])
                idx += 1
            lst.append(tmp)
        
        for i in range(N//2):
            idx = 0
            tmp = []
            while idx < M//2:
                tmp.append(sector1[i][idx])
                idx += 1
            idx = 0
            while idx < M//2:
                tmp.append(sector4[i][idx])    
                idx += 1
            lst.append(tmp)
        return lst


N, M, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
for n in list(map(int, input().split())):
    if n == 1:
        graph = updown(graph[:])
    elif n == 2:
        graph = leftright(graph[:])
    elif n == 3:
        graph = rotate_right(graph[:])
        N, M = M, N
    elif n == 4:
        graph = rotate_left(graph[:])
        N, M = M, N
    elif n == 5:
        graph = divide_rotate(graph[:], 1)
    else:
        graph = divide_rotate(graph[:], 2)
for i in graph:
    print(*i)