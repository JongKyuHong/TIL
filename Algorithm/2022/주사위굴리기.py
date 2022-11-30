import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
moves = list(map(int, input().split()))
dice = [0,0,0,0,0,0]

def dir(i, j, move):
    global x, y
    a,b,c,d,e,f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] # 위, 앞, 왼, 뒤, 오, 아래
    if move == 1 and j+1 < m:
        j += 1
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, d, a, e
        if graph[i][j]:
            dice[5] = graph[i][j]
            graph[i][j] = 0
        else:
            graph[i][j] = dice[5]
        y = j
    elif move == 2 and j-1 >= 0:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, b, a, d, f, c
        j -= 1
        if graph[i][j]:
            dice[5] = graph[i][j]
            graph[i][j] = 0
        else:
            graph[i][j] = dice[5]
        y = j
    elif move == 3 and i-1 >= 0:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, a ,c, f, e, b
        i -= 1
        if graph[i][j]:
            dice[5] = graph[i][j]
            graph[i][j] = 0
        else:
            graph[i][j] = dice[5]
        x = i
    elif move == 4 and i+1 < n:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, a, e, d
        i += 1
        if graph[i][j]:
            dice[5] = graph[i][j]
            graph[i][j] = 0
        else:
            graph[i][j] = dice[5]
        x = i
    else:
        return 0

    return dice

for move in moves:
    aa = dir(x, y, move)
    #print(aa, x, y, 'aa')
    if aa:
        dice = aa[:]
        print(dice[0])
