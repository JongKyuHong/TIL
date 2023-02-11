import sys
input = sys.stdin.readline

N, M = map(int, input().split())
train = [[0]*20 for _ in range(N)]
path = []
for _ in range(M):
    inp = input().split()
    if inp[0] == '1':
        train[int(inp[1])-1][int(inp[2])-1] = 1
    elif inp[0] == '2':
        train[int(inp[1])-1][int(inp[2])-1] = 0
    elif inp[0] == '3':
        for i in range(18, -1, -1):
            train[(int(inp[1])-1)][i+1] = train[(int(inp[1])-1)][i]
        train[(int(inp[1])-1)][0] = 0
    else:
        for i in range(19):
            train[(int(inp[1])-1)][i] = train[(int(inp[1])-1)][i+1]
        train[(int(inp[1])-1)][19] = 0
for i in range(N):
    if train[i] not in path:
        path.append(train[i])
print(len(path))
