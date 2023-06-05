import sys 
input = sys.stdin.readline

def dfs(x, r, g, b, sel):
    global ans, rg, gg, bg
    if sel >= 2:
        ans = min(ans, abs(r//sel-rg)+abs(g//sel-gg)+abs(b//sel-bg))
    for i in range(x+1, N):
        r += r_[i]
        g += g_[i]
        b += b_[i]
        if sel < 7:
            dfs(i, r, g, b, sel+1)
        r -= r_[i]
        g -= g_[i]
        b -= b_[i]

N = int(input())
r_, g_, b_ = [], [], []
for _ in range(N):
    r, g, b = map(int, input().split())
    r_.append(r)
    g_.append(g)
    b_.append(b)
ans = float("inf")
rg,gg,bg = map(int, input().split())
dfs(-1, 0, 0, 0, 0)
print(ans)
