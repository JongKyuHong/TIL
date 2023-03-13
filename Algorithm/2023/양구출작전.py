import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx):
    scount = 0
    for i in arr2[idx]:
        scount += dfs(i)
    if arr[idx][0] == 'S' and idx != 1:
        scount += arr[idx][1]
    elif arr[idx][0] == 'W':
        scount = scount - arr[idx][1]
    if scount <= 0:
        scount = 0
    return scount
N = int(input())
arr = [[],[0, 0]]
arr2 = [[] for i in range(N+2)]
for i in range(2, N+1):
    t, a, p = input().rstrip().split()
    a = int(a)
    p = int(p)
    arr.append([t, a, p])
    arr2[p].append(i)

res = dfs(1)
print(res)