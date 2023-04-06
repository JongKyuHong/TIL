import sys
input = sys.stdin.readline

N, M = map(int, input().split())
switch = []
for _ in range(N):
    lst = list(map(int, input().split()))
    #switch[lst[0]] = lst[1:]
    switch.append(lst)

for i in range(N):
    visited = [0]*(M+1)
    for j in range(N):
        if i == j:
            continue
        else:
            for k in switch[j][1:]:
                visited[k] = 1
    flag = 0
    for j in range(1,M+1):
        if not visited[j]:
            flag = 1
    if not flag:
        print(1)
        exit()
print(0)


