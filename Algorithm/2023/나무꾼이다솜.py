import sys
input = sys.stdin.readline

N, C, W = map(int, input().split())
tree = [int(input()) for _ in range(N)]
max_v = 0
for i in range(1, max(tree)+1):
    ans = 0
    for j in tree:
        cnt, remain = divmod(j, i)
        if remain:
            ex = cnt*C
        else:
            ex = (cnt-1)*C
        target = (cnt*W*i) - ex
        if target < 0:
            continue
        ans += target
    max_v = max(max_v, ans)
print(max_v)