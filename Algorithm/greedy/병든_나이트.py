n, m = map(int,input().split())

array = [[0]*m for i in range(n)]
x,y = n-1,0 # 가장 왼쪽 아래
dx = [-2,-1,1,2]
dy = [1,2,2,1]
def check(x,y):
    print('hi')
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx <= n or nx >= 0) and (ny <= m or ny >= 0):
            if i == 0:
                array[x-1][y] = 1
                array[x-2][y] = 1
                array[x-2][y] = 1
                check(nx,ny)
            elif i == 1:
                array[x-1][y] = 1
                array[x-1][y+1] = 1
                array[x-1][y+1] = 1
                check(nx,ny)
            elif i == 2:
                array[x+1][y] = 1
                array[x+1][y+1] = 1
                array[x+1][y+2] = 1
                check(nx,ny)
            else:
                array[x+1][y] = 1
                array[x+2][y] = 1
                array[x+2][y+1] = 1
                check(nx,ny)
        else:
            return False
    return array
count = 0
result_array = check(x,y)
for i in result_array:
    for j in i:
        if j == 1:
            count += 1
print(count)
