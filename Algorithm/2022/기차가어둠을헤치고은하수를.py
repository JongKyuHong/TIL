n, m = map(int, input().split())
train = [[0]*20 for _ in range(n)]

for i in range(m):
    command = list(map(int, input().split()))
    if command[0] == 1:
        train[command[1] - 1][command[2]-1] = 1
    elif command[0] == 2:
        train[command[1] - 1][command[2]-1] = 0
    elif command[0] == 3:
        tmp = 0
        for i in range(1, 20):
            tmp = train[command[1] - 1][i]
            train[command[1] - 1][i] = train[command[1] - 1][i-1]
    else:
        tmp = 0
        for i in range(19, -1, -1):
            tmp = train[command[1] - 1][i-1]
            train[command[1] - 1][i-1] = train[command[1] - 1][i]

print(train)