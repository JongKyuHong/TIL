from collections import deque
import sys
input = sys.stdin.readline

n = int(input()) # 정점 갯수
graph = [[]*(n+1) for _ in range(n+1)]
parent = [0 for i in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    parent[v] = u

# 자식 갯수가 많은 애부터 얼리어답터
dp = [0]*(n+1)
while 1:
    max_v, max_i = 0, 0
    for i in range(1,n+1):
        #print(graph[i], max_v, len(graph[i]), dp[i],'asdf')
        if graph[i] and max_v <= len(graph[i]) and not dp[i]:
            max_v = len(graph[i])
            max_i = i
    print(max_i,'idx')
    dp[max_i] = 1
    cycle_flag = 1
    for i in range(1, n+1):
        if not dp[i]:
            if i == 1:
                if graph[i]:
                    flag = 1
                    for j in graph[i]:
                        if not dp[j]:
                            flag = 0
                            break
                    if not flag:
                        cycle_flag = 0
                        break
            elif i == n:
                if not dp[parent[n]]:
                    cycle_flag = 0
                    break
            else:
                if dp[parent[i]] and graph[i]:
                    flag = 1
                    for j in graph[i]:
                        if not dp[j]:
                            flag = 0
                            break
                    if not flag:
                        cycle_flag = 0
                        break
    if cycle_flag == 1:
        break

print(dp)
        # if dp[parent[i]] and graph[i]: # 부모가 얼답이고, 자식이 있고 만약
        #     for j in graph[i]: # 자식이 얼답이면
        #         if dp[j] 
    





