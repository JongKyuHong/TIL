import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(node, val):
    cnt = 0
    for i in tree[node]:
        if not visited[i]:
            cnt += 1
    if cnt == 0:
        global ans_val, ans_cnt
        ans_val += val
        ans_cnt += 1
        return
    v = val//cnt
    r = val%cnt
    cc = 0
    for i in tree[node]:
        if not visited[i]:
            cc += 1
            visited[i] = 1
            if cc == cnt:
                find(i, v+r)
            else:
                find(i, v)
        
N, W = map(int, input().split())
tree = [[] for _ in range(N+1)]
ans_val, ans_cnt = 0, 0
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [0]*(N+1)
visited[1] = 1
find(1, W)

print(ans_val/ans_cnt)