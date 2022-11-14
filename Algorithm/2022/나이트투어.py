import sys
input = sys.stdin.readline

graph = [[0]*6 for _ in range(6)]
visited = [[0]*6 for _ in range(6)]
delta = ((1,2),(1,-2),(-1,2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1))
start_r, start_c = 0, 0
for i in range(36):
    data = input().rstrip()
    if i == 0:
        c, r = ord(data[0])-65, int(data[1])-1
        start_r, start_c = r, c
        visited[r][c] = 1
    else:
        dc, dr = ord(data[0])-65, int(data[1])-1
        flag = 1
        for nr, nc in delta:
            if 0 <= r + nr < 6 and 0 <= c + nc < 6 and r + nr == dr and c + nc == dc and not visited[r+nr][c+nc]:
                flag = 0
                break
        if not flag:
            r, c = dr, dc
            visited[r][c] = 1
        else:
            print('Invalid')
            exit()
flag = 1
dr, dc = start_r, start_c
for nr, nc in delta:
    if 0 <= r + nr < 6 and 0 <= c + nc < 6 and r + nr == dr and c + nc == dc:# and not visited[r+nr][c+nc]:
        flag = 0
        break
if not flag:
    print('Valid')
else:
    print('Invalid')
    exit()