# 순환하지 않는 방향 그래프에 대해서만 사용가능합니다.
# 여러가지 답이 존재 할 수 있습니다. (한의 단계에서 큐에 새롭게 들어가는 원소가 2개이상인경우)
# 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있습니다. (사이클에 속한 원소는 큐에 들어올 수
# 없으므로)
from collections import deque

# 노드의 갯수와 간선의 갯수
v, e = map(int, input().split())
# 모든 노드의 대한 진입차수 0초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v+1)]

# 방향 그래프의 모든 간선정보 입력받음
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 a에서 b로 이동가능
    # 진입 차수 1증가
    indegree[b] += 1

def topology_sort():
    result = [] 
    q = deque()
    # 초기에는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소에 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입한다.
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=' ')
            
topology_sort()


