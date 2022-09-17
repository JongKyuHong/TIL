r, s = map(int, input().split())

graph = [input() for _ in range(r)]

col = [0]*s

value = float('inf')
for i in range(s):
    cnt, cnt2 = -1, -1
    for j in range(r):
        if graph[j][i] == 'X':
            cnt = j
        elif graph[j][i] == '#':
            cnt2 = j
            break
    if cnt == -1 or cnt2 == -1:
        continue
    value = min(value, cnt2-cnt-1)

def made(value):
    graph2 = [['.']*s for _ in range(r)]
    for i in range(r):
        for j in range(s):
            if graph[i][j] == 'X':
                graph2[i+value][j] = 'X'
            elif graph[i][j] == '#':
                graph2[i][j] = '#'
    return graph2

graph3 = made(value)
for i in graph3:
    print(''.join(i))
