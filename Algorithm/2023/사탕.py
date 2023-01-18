import sys
input = sys.stdin.readline

for _ in range(int(input())):
    J, N = map(int, input().split()) # 사탕의 개수, 상자의 개수
    candy = []
    for _ in range(N):
        r, c = map(int, input().split())
        candy.append(r*c)
    candy.sort(reverse=True)
    cnt = 0
    for i in candy:
        J -= i
        cnt += 1
        if J <= 0:
           break
    print(cnt)