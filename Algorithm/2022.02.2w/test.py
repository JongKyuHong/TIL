import sys
read = sys.stdin.readline

def BFS(startV):
    q = [startV]
    length[startV] = 0
    while len(q):
        nowV = q.pop(0)
        for nextV in friends[nowV]:
            if length[nextV] > length[nowV]:
                length[nextV] = length[nowV] + 1
                q.append(nextV)


N = int(read())
L = int(read())
friends = [[] for _ in range(N+1)]      #인접 리스트
length = [999 for _ in range(N+1)]      #방문 체크 겸 depth
for _ in range(L):
    a, b = map(int, read().split())
    friends[a].append(b)
    friends[b].append(a)

BFS(1)
ans = 0
for i in range(1, N+1):
    if length[i] in [1, 2]:
        ans += 1
print(ans)