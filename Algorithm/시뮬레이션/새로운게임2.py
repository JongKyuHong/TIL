import sys 
input = sys.stdin.readline
delta = ((0, 1), (0, -1), (-1, 0), (1, 0))

def find_location(raw_key, r, c, now_delta, cnt, tmp):
    global flag
    dr, dc = delta[now_delta]
    nr, nc = r+dr, c+dc
    if nr >= N or nr < 0 or nc >= N or nc < 0 or graph[nr][nc] == 2: # 파란색인경우
        if cnt == 0:
            if now_delta % 2 == 0:
                find_location(raw_key, r, c, now_delta+1, cnt+1, tmp)
            else:
                find_location(raw_key, r, c, now_delta-1, cnt+1, tmp)
        else: # 1인데 또 파랑만남
            for k2, d2 in tmp:
                if raw_key == k2:
                    lst[r][c].append([k2, now_delta])
                else:
                    lst[r][c].append([k2, d2])
                key_locate[k2] = [r, c]
    elif graph[nr][nc] == 0: # 흰색 그냥 지속
        for k2, d2 in tmp:
            if raw_key == k2:
                lst[nr][nc].append([k2, now_delta])
            else:
                lst[nr][nc].append([k2, d2])
            key_locate[k2] = [nr, nc]
    elif graph[nr][nc] == 1: # 빨간색인경우
        tmp.reverse()
        for k2, d2 in tmp:
            if raw_key == k2:
                lst[nr][nc].append([k2, now_delta])
            else:
                lst[nr][nc].append([k2, d2])
            key_locate[k2] = [nr, nc]
    if 0 <= nr < N and 0 <= nc < N:
        if len(lst[nr][nc]) >= 4:
            flag = 1

N, K = map(int, input().split())
key_locate = {}
#graph = [[[] for _ in range(N)] for _ in range(N)]
graph = [list(map(int, input().split())) for _ in range(N)]
lst = [[[] for _ in range(N)] for _ in range(N)]


for i in range(1, K+1):
    r, c, d = map(int, input().split())
    r -= 1; c -= 1; d -= 1
    lst[r][c].append([i, d])
    key_locate[i] = [r, c]

turn = 0
flag = -1
while turn < 1000:
    turn += 1
    #for k, v in sorted(key_locate.items(), key=lambda x: x[0]):#key_locate.items():
    for k in range(1, K+1):
        r, c = key_locate[k]
        cnt_value = 0
        tmp_value = 0
        for k_, d_ in lst[r][c]:
            if k_ == k:
                tmp_value = len(lst[r][c]) - cnt_value
                break
            cnt_value += 1
        
        if tmp_value > 1: # k뒤에 뭐가 더 있으면
            tmp = []
            # cnt_value 사실상 이게 인덱스 이거 뒤로 다
            for _ in range(tmp_value):
                tmp_k, tmp_d = lst[r][c].pop()
                tmp.append([tmp_k, tmp_d])
            tmp.reverse()
            now_delta = tmp[0][1]
            find_location(k, r, c, now_delta, 0, tmp)
        else: # 뒤에 아무것도 없으면 본인만 이동
            # tmp_k, tmp_d = lst[r][c].pop()
            tmp_k, tmp_d = lst[r][c].pop()
            find_location(k, r, c, tmp_d, 0, [[tmp_k, tmp_d]])
        if flag == 1: # 이미 4개 넘음
            print(turn)
            exit()
print(-1)


