import sys 
input = sys.stdin.readline

def rotate(sticker):
    r, c = len(sticker), len(sticker[0])
    new_sticker = [[0]*r for _ in range(c)] # 90도 회전이므로 행과 열이 바뀜
    # 돌리기 전 1행이 돌린 후의 마지막 열로 들어가야 한다.

    for i in range(r):
        for j in range(c):
            new_sticker[j][r-i-1] = sticker[i][j]

    return new_sticker

def check(i, j, r, c, sticker): # 왼쪽위가 i, j값인 lst에서 r, c 크기의 스티커를 붙일 수 있는지 확인
    if i+r > N or j+c > M:
        return 0
    for k in range(i, i+r, 1):
        for l in range(j, j+c, 1):
            if sticker[k-i][l-j] == 1:
                if lst[k][l] == 1:
                    return 0
                
    for k in range(i, i+r, 1):
        for l in range(j, j+c, 1):
            if sticker[k-i][l-j] == 1:
                lst[k][l] = 1
    return 1

N, M , K = map(int, input().split())

lst = [[0]*M for _ in range(N)]

stickers = []
for i in range(K):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    stickers.append(sticker)

for sticker in stickers:
    for _ in range(4):
        r, c = len(sticker), len(sticker[0])
        # 지금 이게 lst에 딱 들어가는지
        flag = 0
        for i in range(N):
            for j in range(M):
                if check(i, j, r, c, sticker): # true면 들어 갈 수 있음
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 1:
            break
        sticker = rotate(sticker)

answer = 0
for i in lst:
    answer += sum(i)
print(answer)