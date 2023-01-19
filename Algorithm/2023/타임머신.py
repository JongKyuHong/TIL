import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

distance = [float('inf')] * (N+1)
def bellman_ford(start):
    distance[start] = 0
    for i in range(N):
        for j in range(M):
            cur_node = graph[j][0]
            next_node = graph[j][1]
            edge_cost = graph[j][2]
            if distance[cur_node] != float('inf') and distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                if i == N-1:
                    return 1
    return 0
negative_cycle = bellman_ford(1)
if negative_cycle:
    print('-1')
else:
    for i in range(2, N+1):
        if distance[i] == float('inf'):
            print('-1')
        else:
            print(distance[i])