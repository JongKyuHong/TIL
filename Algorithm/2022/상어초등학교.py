from collections import deque
n = int(input())
graph = [[-1]*n for _ in range(n)]
favo_graph = [[0]*n for _ in range(n)]
delta = ((0,1),(0,-1),(1,0),(-1,0))
input_array = [list(map(int, input().split())) for _ in range(n*n)]

def search(r, c, favorite):
    q = deque([])
    between, favo = 0, 0
    q.append((r,c,between))
    while q:
        r, c, between = q.popleft()
        for dr, dc in delta:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < n and 0 <= nc < n:
                if graph[nr][nc] == -1:
                    between += 1
                else:
                    if graph[nr][nc] in favorite:
                        favo += 1
    return [between, favo]

for i in range(n*n):
    # nums = list(map(int, input().split()))
    # num = nums[0]
    # favorite = nums[1:]
    num = input_array[i][0]
    favorite = input_array[i][1:]
    between, favo, br, bc, favo_count = -1, -1, -1, -1, -1
    for j in range(n):
        for k in range(n):
            if graph[j][k] == -1:
                between_value, favo_value = search(j, k, favorite)
                if favo_value > favo:
                    between, favo, br, bc = between_value, favo_value, j, k
                elif favo_value == favo:
                    if between_value > between:
                        between, br, bc = between_value, j, k
                    elif between_value == between:
                        if br > j:
                            br, bc = j, k
                        elif br == j:
                            if bc > k:
                                bc = k
    graph[br][bc] = num

res = 0
for j in range(n):
    for k in range(n):
        flag = 0
        for i in range(n*n):
            if graph[j][k] == input_array[i][0]:
                flag = 1
                between, favo = search(j, k, input_array[i][1:])
                if favo == 1:
                    res += 1
                elif favo == 2:
                    res += 10
                elif favo == 3:
                    res += 100
                elif favo == 4:
                    res += 1000
            if flag:
                break
print(res)