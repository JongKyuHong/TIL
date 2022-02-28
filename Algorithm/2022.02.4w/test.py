def findcores(array):
    fix = 0
    cores = []
    for r in range(n):
        for c in range(n):
            if array[r][c]:
                if r == 0 or r == n-1 or c == 0 or c == n-1:
                    fix += 1
                else:
                    cores.append((r,c))
    return fix, cores

def dfs(now, last, code):
    global maxCores, minCode
    if maxCores < len(now):
        maxCores = len(now)
        minCode = 12*12+1
    if maxCores == len(now) and minCode > code:
        minCode = code
    

for test_case in range(int(input())):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    fix, cores = findcores(array)
    maxCores = -1
    minCode = 12*12+1
    dfs([], 0, 0)