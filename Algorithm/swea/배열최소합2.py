t = int(input())


def dfs(row,sum_value):
    global mina
    if row == n:  # 제일 밑에 도달한 경우
        mina = min(sum_value,mina)  # mina와 sum_value중 낮은 값을 반환
        return mina
    if sum_value > mina:  # 이미 sum_value가 mina보다 크면 의미가 없는 값이므로 중단
        return -1
    for i in range(n):
        if visited[i] == False:  # 방문하지 않은 열일때
            sum_value += graph[row][i]
            visited[i] = True  # 가거나
            dfs(row+1,sum_value)  
            visited[i] = False  # 안가거나
            sum_value -= graph[row][i]
    

for test_case in range(1,t+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    visited = [False for _ in range(n)]  # 열에 방문하였는지 체크
    mina = 101  # 최소합
    sum_value = 0  # 합저장
    dfs(0,sum_value)
    print(f'#{test_case} {mina}')




