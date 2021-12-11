t = int(input())

def dfs(s,visited,array):
    visited[s] = True  # 방문처리
    for i in array[s]:  # 해당 인덱스의 다른값에도 접근 즉, 인접한 다른노드 확인
        if visited[i] == False:  # 아직 방문하지 않은 곳이 있다면
            dfs(i,visited,array)  # 재귀호출

for test_case in range(1,t+1):
    v,e = map(int,input().split())
    array = [[] for _ in range(v+1)]  # 그래프 생성
    for _ in range(e):
        start,end = map(int,input().split())  # 출발도착노드 받음
        array[start].append(end)  # 출발노드안에 도착노드 추가 (하나의 출발지에서 여러곳으로 도달할수있기때문에)
    s,g = map(int,input().split())  # 시작점 노드와 도착지점 노드
    visited = [False for _ in range(v+1)]  # 방문여부를 저장해놓음
    dfs(s,visited,array)  # dfs 함수로 구현
    ans = 0
    if visited[g]:  # 도착지점을 방문하였으면 1로 출력
        ans = 1
    print(f'#{test_case} {ans}')



