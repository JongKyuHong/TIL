import sys
input = sys.stdin.readline

def find(cnt, cc):
    global max_v, ans, ans_M
    if cc == M:
        ans_M = min(ans_M, cnt)
    elif cc > max_v and cc != 0:
        max_v = cc
        ans = cnt
    elif cc == max_v:
        if ans > cnt:
            ans = cnt

    for i in range(N):
        if not visited_guitar[i]:
            visited_guitar[i] = 1
            name, song = lst[i]
            c = 0
            aa = []
            for j in range(M):
                if song[j] == 'Y' and not visited[j]:
                    visited[j] = 1
                    c += 1
                    aa.append(j)
            find(cnt+1, cc+c)
            for j in aa:
                visited[j] = 0
            visited_guitar[i] = 0

N, M = map(int, input().split())
visited = [0]*M
visited_guitar = [0]*N
lst = []
ans, max_v, ans_M = float('inf'), -1, float('inf')
for _ in range(N):
    name, song = input().rstrip().split()
    lst.append((name, song))

find(0, 0)
if ans_M == float('inf'):
    print(ans if ans != float('inf') else -1)
else:
    print(ans_M)
##print(ans if ans != float('inf') else -1)