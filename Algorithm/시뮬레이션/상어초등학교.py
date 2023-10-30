import sys 
input = sys.stdin.readline
delta = ((0, 1), (0, -1), (1, 0), (-1, 0))#, (1, 1),(1, -1), (-1, 1), (-1, -1))

N = int(input())
lst = []
dic = {}
for _ in range(N*N):
    num, a, b, c, d = map(int, input().split())
    lst.append([num, a, b, c, d])
    dic[num] = [a, b, c, d]

graph = [[0]*N for _ in range(N)]
# 1. 좋아하는 학생이 가장 많은 칸
# 2. 1을 만족하는 칸이 여러개면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 3. 2를 만족하는 칸도 여러개면 행의 번호가 가장 작은칸, 그런 칸도 여러개면 가장 열이 작은

for num, A, B, C, D in lst:
    max_v = 0
    max_v_lst = []

    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                continue
            tmp = 0
            zero_cnt = 0
            for dr, dc in delta:
                nr, nc = dr+i, dc+j
                if 0 <= nr < N and 0 <= nc < N:
                    if graph[nr][nc] in [A, B, C, D]:
                        tmp += 1
                    elif graph[nr][nc] == 0:
                        zero_cnt += 1
            if max_v < tmp:
                max_v = tmp
                max_v_lst.clear()
                max_v_lst.append([zero_cnt, i, j])
            elif max_v == tmp:
                max_v_lst.append([zero_cnt, i, j])
    if len(max_v_lst) == 1:
        r, c = max_v_lst[0][1], max_v_lst[0][2]
        graph[r][c] = num
    else: # 여러개라면
        # 근처 0개수 판단 및 행번호 열번호가 가장 작은게 첫번째 값임
        max_v_lst.sort(key=lambda x:x[0], reverse=True)
        r, c = max_v_lst[0][1], max_v_lst[0][2]
        graph[r][c] = num

answer = 0
score = {0:0, 1:1, 2:10, 3:100, 4:1000}
for i in range(N):
    for j in range(N):
        tmp = dic[graph[i][j]]
        cnt = 0
        for dr, dc in delta:
            nr, nc = dr+i, dc+j
            if 0 <= nr < N and 0 <= nc < N: # 
                if graph[nr][nc] in tmp:
                    cnt += 1
        answer += score[cnt]
print(answer)
                    
