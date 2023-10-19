import sys 
input = sys.stdin.readline

def find(x):
    visited[x] = 1
    y = parent[x]
    if not visited[y]:
        find(y)
    elif not finished[y]: # 사이클이 존재할때
        while y != x:
            cycle.append(y)
            y = parent[y]
        cycle.append(x)
    finished[x] = 1    

N = int(input())
parent = [0] + [int(input()) for _ in range(N)]
visited = [0] * (N+1)
finished = [0]*(N+1)
answer = 0
answer_lst = []
tmp = 0
tmp_lst = []
for i in range(1, N+1):
    if i == parent[i]:
        visited[i] = 1
        finished[i] = 1
        tmp += 1
        tmp_lst.append(i)
for i in range(1, N+1):
    if not visited[i]:
        cycle = []
        find(i)
        if cycle:
            tmp_lst = tmp_lst + cycle
            tmp += len(cycle)

print(tmp)
for i in sorted(tmp_lst):
    print(i)
# 가장 큰 사이클을 판단하라?
# 방문하지 않은 노드부터 사이클을 돌며 몇개의 노드가 이 사이클에 들어있는지 확인 후 글로벌 변수와 비교해서 최대를 찾는다.
