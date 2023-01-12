from collections import defaultdict
import sys
input = sys.stdin.readline

while 1:
    n, k = map(int, input().split()) # 노드수, 사촌을 구해야하는 노드의 수
    if n == 0 and k == 0:
        break
    lst = list(map(int, input().split()))
    root = lst[0]
    stack = [[] for _ in range(n)]
    stack[0].append(root)
    level = 1
    tmp = 0
    idx = 1
    level_value = 0
    par = defaultdict(int) # 부모노드 저장
    while idx < n:
        if tmp != 0 and tmp+1 != lst[idx]:
            level_value += 1
            if level_value == len(stack[level-1]):
                level += 1
                level_value = 0
        stack[level].append(lst[idx])
        par[lst[idx]] = stack[level-1][level_value]
        tmp = lst[idx]
        idx += 1
    res = 0
    for i in range(n):
        if k in stack[i]:
            parent = par[k]
            for j in range(len(stack[i])):
                if par[stack[i][j]] == parent:
                    continue
                else:
                    if par[par[stack[i][j]]] == par[parent]:
                        res += 1

            break
    print(res)