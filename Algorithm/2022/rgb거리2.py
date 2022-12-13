import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')

def check(idx):
    global answer
    dp2 = [[float('inf')]*3 for _ in range(n)]
    dp2[0][idx] = graph[0][idx]
    for i in range(1, n-1):
        for j in range(3):
            if j == 0:
                dp2[i][j] = min(dp2[i-1][1], dp2[i-1][2]) + graph[i][j]
            elif j == 1:
                dp2[i][j] = min(dp2[i-1][0], dp2[i-1][2]) + graph[i][j]
            else:
                dp2[i][j] = min(dp2[i-1][0], dp2[i-1][1]) + graph[i][j]

    if dp2[0][0] != float("inf"):
        dp2[n-1][1] = min(dp2[n-2][0], dp2[n-2][2]) + graph[n-1][1]
        dp2[n-1][2] = min(dp2[n-2][0], dp2[n-2][1]) + graph[n-1][2]
    elif dp2[0][1] != float("inf"):
        dp2[n-1][0] = min(dp2[n-2][1], dp2[n-2][2]) + graph[n-1][0]
        dp2[n-1][2] = min(dp2[n-2][0], dp2[n-2][1]) + graph[n-1][2]
    else:
        dp2[n-1][1] = min(dp2[n-2][0],dp2[n-2][2]) + graph[n-1][1]
        dp2[n-1][0] = min(dp2[n-2][1],dp2[n-2][2]) + graph[n-1][0]
    answer = min(answer, min(dp2[n-1]))

for i in range(3):
    check(i)


print(answer)