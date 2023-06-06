import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(N)]
ans = -1
if N == 1 and M == 1:
    int_num = int(lst[0][0])
    if int(int_num**(1/2)) == int_num**(1/2):
        ans = max(ans, int_num)
# 행 고정 검사
for j in range(1, M):
    for r in range(N):
        for k in range(M):
            num = ''
            c = k
            while 0 <= r < N and 0 <= c < M:
                num += lst[r][c]
                c += j
                int_num = int(num)
                if int(int_num**(1/2)) == int_num**(1/2):
                    ans = max(ans, int_num)
    for r in range(N):
        for k in range(M-1, -1, -1):
            num = ''
            c = k
            while 0 <= r < N and 0 <= c < M:
                num += lst[r][c]
                c -= j
                int_num = int(num)
                if int(int_num**(1/2)) == int_num**(1/2):
                    ans = max(ans, int_num)

# 열 고정 검사
for i in range(1, N):
    for k in range(N):
        for c in range(M):
            num = ''
            r = k
            while 0 <= r < N and 0 <= c < M:
                num += lst[r][c]
                r += i
                int_num = int(num)
                if int(int_num**(1/2)) == int_num**(1/2):
                    ans = max(ans, int_num)

    for k in range(N-1, -1, -1):
        for c in range(M):
            num = ''
            r = k
            while 0 <= r < N and 0 <= c < M:
                num += lst[r][c]
                r -= i
                int_num = int(num)
                if int(int_num**(1/2)) == int_num**(1/2):
                    ans = max(ans, int_num)
# 대각도 봐야함
target = min(N, M)
gap = 0
idx = 0
# 0, 0에서 시작해서 0, 1 0, 2 이런순으로 가는경우
# 행과 열이 균등하게 증가하지 않아도 되었음

for i in range(1, N): # 행의 gap
    for j in range(1, M): # 열의 gap
        for k in range(N):
            for l in range(M):
                # + +
                num = ''
                r, c = k, l
                while 0 <= r < N and 0 <= c < M:
                    num += lst[r][c]
                    r += i
                    c += j
                    int_num = int(num)
                    if int(int_num**(1/2)) == int_num**(1/2):
                        ans = max(ans, int_num)
        for k in range(N-1, -1, -1):
            for l in range(M):
                # - +
                num = ''
                r, c = k, l
                while 0 <= r < N and 0 <= c < M:
                    num += lst[r][c]
                    r -= i
                    c += j
                    int_num = int(num)
                    if int(int_num**(1/2)) == int_num**(1/2):
                        ans = max(ans, int_num)
        for k in range(N):
            for l in range(M-1, -1, -1):
                # + -
                num = ''
                r, c = k, l
                while 0 <= r < N and 0 <= c < M:
                    num += lst[r][c]
                    r += i
                    c -= j
                    int_num = int(num)
                    if int(int_num**(1/2)) == int_num**(1/2):
                        ans = max(ans, int_num)

        for k in range(N-1,-1,-1):
            for l in range(M-1,-1,-1):
                # - -
                num = ''
                r, c = k, l
                while 0 <= r < N and 0 <= c < M:
                    num += lst[r][c]
                    r -= i
                    c -= j
                    int_num = int(num)
                    if int(int_num**(1/2)) == int_num**(1/2):
                        ans = max(ans, int_num)
print(ans)