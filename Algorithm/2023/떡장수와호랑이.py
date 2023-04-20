import sys
input = sys.stdin.readline

def find(depth, idx, lst):
    if depth == N+1:
        for i in lst:
            print(i)
        exit()
    for i in day[depth]:
        if i != idx and not visited[depth][i]:
            visited[depth][i] = 1
            find(depth+1, i, lst+str(i))
    
N = int(input())
day = {}
for i in range(1, N+1):
    input_data = list(map(int, input().split()))
    day[i] = input_data[1:]

visited = [[0 for _ in range(10)] for i in range(N+1)]
find(1, -1, '')
print(-1)