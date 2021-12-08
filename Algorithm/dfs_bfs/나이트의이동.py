from collections import deque

test_case = int(input())
delta = ((-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1))

def start(r,c,dr,dc,graph):
    q = deque()
    q.append((r,c,0))
    graph[r][c] = 1
    target = float('inf')
    while q:
        r,c,count = q.popleft()
        for dr2, dc2 in delta:
            nr = r + dr2
            nc = c + dc2
            count2 = count + 1
            if 0 <= nr < l and 0 <= nc < l and not graph[nr][nc]:
                graph[nr][nc] = 1
                if nr == dr and nc == dc:
                    target = min(target, count2)
                else:
                    q.append((nr, nc, count2))
    return target

for _ in range(test_case):
    l = int(input())
    graph = [[0]*l for _ in range(l)]
    r, c = map(int, input().split())
    dr, dc = map(int, input().split())
    if r == dr and c == dc:
        print(0)
    else:
        target = start(r,c,dr,dc,graph)
        print(target)


