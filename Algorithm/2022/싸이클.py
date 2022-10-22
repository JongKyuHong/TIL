import sys
input = sys.stdin.readline

N, P = map(int, input().split())
res = []
ans = N
while 1:
    ans = (ans*N)%P
    if ans not in res:
        res.append(ans)
    else:
        print(len(res)-res.index(ans))