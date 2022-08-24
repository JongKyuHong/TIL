import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n은 아이스크림 종류의 수, m은 섞어먹으면 안되는 조합의 갯수
ice = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    ice[a].append(b)
    ice[b].append(a)

s1 = set()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j or j in ice[i]:
            continue
        for k in range(1,n+1):
            if i == k or j == k or k in ice[i] or k in ice[j]:
                continue
            s1.add((i,j,k))
print(s1)