import sys
input = sys.stdin.readline

n = int(input())
dura = [0] * n
weight = [0] * n

for i in range(n):
    a, b = map(int, input().split())
    dura[i] = a
    weight[i] = b

res = 0
def dfs(idx):
    global res
    if idx == n:
        cnt = 0
        for i in dura:
            if i <= 0:
                cnt += 1
        res = max(res, cnt)
        return
    if dura[idx] <= 0:
        dfs(idx+1)
        return

    for i in range(n):
        if i == idx:
            continue
        if dura[i] > 0:
            dura[idx] -= weight[i]
            dura[i] -= weight[idx]
            dfs(idx+1)
            dura[idx] += weight[i]
            dura[i] += weight[idx]
        else:
            dfs(idx+1)
        
dfs(0)
print(res)