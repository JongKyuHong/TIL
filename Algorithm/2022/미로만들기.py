import sys
input = sys.stdin.readline


n = int(input())
word = input().rstrip()
graph = [[0]*103 for _ in range(103)]
row, col = 51, 51
graph[51][51] = 1

delta = ((1,0),(0,-1),(-1,0),(0,1))
max_row, max_col = row, col
min_row, min_col = row, col
dir = 0

path = []
for i in word:
    if i == 'R':
        dir += 1
        dir%=4
    elif i == 'L':
        dir -= 1
        dir%=4
    elif i == 'F':
        row, col = row+delta[dir][0], col+delta[dir][1]
        graph[row][col] = 1
        max_row = max(max_row, row)
        max_col = max(max_col, col)
        min_row = min(min_row, row)
        min_col = min(min_col, col)

for i in range(min_row, max_row+1):
    for j in range(min_col, max_col+1):
        if graph[i][j] == 1:
            print('.',end='')
        else:
            print('#',end='')
    print()
