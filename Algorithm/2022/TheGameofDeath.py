import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input()) # 플레이어의 숫자
    lst = [0] + list(int(input()) for _ in range(n))
    cnt = 0
    idx = 1
    while 1:
        cnt += 1
        if cnt > n:
            print(0)
            break
        if lst[idx] == n:
            print(cnt)
            break
        idx = lst[idx]
    