import sys 
input = sys.stdin.readline
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

def coordinate_transformation(r, c, d, s):
    r, c = (r+(dr[d]*s))%N, (c+(dc[d]*s))%N
    lst[r][c] += 1
    return (r, c)

def waterbug(r, c):
    cnt = 0
    if 0 <= r+1 < N and 0 <= c+1 < N and lst[r+1][c+1] >= 1:
        cnt += 1
    if 0 <= r+1 < N and 0 <= c-1 < N and lst[r+1][c-1] >= 1:
        cnt += 1
    if 0 <= r-1 < N and 0 <= c+1 < N and lst[r-1][c+1] >= 1:
        cnt += 1
    if 0 <= r-1 < N and 0 <= c-1 < N and lst[r-1][c-1] >= 1:
        cnt += 1
    return cnt

def delete_cloud():
    tmp = set()
    for i in range(N):
        for j in range(N):
            if (i, j) not in visited and lst[i][j] >= 2:
                lst[i][j] -= 2
                tmp.add((i, j))
    return tmp

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
location = [list(map(int, input().split())) for _ in range(M)]
cloud = ((N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1))
cnt = 0
for d, s in location:
    # 비바라기 시전
    d -= 1
    visited = set()
    for r, c in cloud:
        r1, c1 = coordinate_transformation(r, c, d, s)

    for r, c in visited:
        lst[r][c] += waterbug(r, c)

    cloud = delete_cloud()
answer = 0
for i in lst:
    answer += sum(i)
print(answer)