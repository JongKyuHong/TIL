n, m = map(int, input().split())
train = [[0]*20 for _ in range(n)]
state = []

for i in range(m):
    command = list(map(int, input().split()))
    if command[0] == 1:
        train[command[1] - 1][command[2]-1] = 1
    elif command[0] == 2:
        train[command[1] - 1][command[2]-1] = 0
    elif command[0] == 3:
        for j in range(19, 0, -1):
            train[command[1] - 1][j] = train[command[1] - 1][j - 1]
        train[command[1] - 1][0] = 0
    else:
        for j in range(19):
            train[command[1] - 1][j] = train[command[1] - 1][j + 1]
        train[command[1] - 1][19] = 0

cnt = 0
for i in range(n):
    if train[i] not in state:
        state.append(train[i])
        cnt += 1

print(cnt)