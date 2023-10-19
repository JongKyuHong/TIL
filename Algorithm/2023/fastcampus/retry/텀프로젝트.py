import sys 
input = sys.stdin.readline

def find(x):
    visited[x] = 1
    if not visited[parent[x]]:
        find(parent[x])
    elif not finished[parent[x]]:
        while parent[x] != x:
            result.append(parent[x])
            parent[x] = parent[parent[x]]
        result.append(x)
    finished[x] = 1
T = int(input())
for _ in range(T):
    N = int(input())
    parent = [0] + list(map(int, input().split()))
    visited = [0]*(N+1)
    finished = [0]*(N+1)
    answer = 0
    result = []
    for i in range(1,N+1):
        if not visited[i]:
            find(i)
    print(N-len(result))

        
# 싸이클을 못만드는 노드의 갯수를 찾아서 출력
# 싸이클은 union-find로 찾을 수 있다.
# 어떤 노드랑 union할것인가


