n,m = map(int,input().split())

dx = [1,2,2,1]  # 리스트에서 x좌표는 실제로는 y좌표를뜻한다.
dy = [-2,-1,1,2]
graph = [[0]*m for _ in range(n)]
y,x = [n-1,0]  # 현재위치
def check(y,x):
    global count
    for i in range(4):
        if x + dx[i] < 0 or x+dx[i] >= m or y + dy[i] < 0 or y + dy[i] >=n : # m같은 경우는 같아도 안된다 마지막 행의 인덱스가 49이기때문 (예제1번기준)
            continue
        else:
            if i == 0:
                print('0번')
                graph[y][x] == 1
                graph[y-1][x] == 1
                graph[y-2][x] == 1
                graph[y-2][x+1] == 1
                nx = x+dx[i]
                ny = y+dy[i]
                return check(ny,nx)
            elif i == 1:
                print('1번')
                graph[y][x] == 1
                graph[y-1][x] == 1
                graph[y-1][x+1] == 1
                graph[y-1][x+2] == 1
                nx = x+dx[i]
                ny = y+dy[i]
                return check(ny,nx)
            elif i == 2:
                print('3번')
                graph[y][x] == 1
                graph[y+1][x] == 1
                graph[y+1][x+1] == 1
                graph[y+1][x+2] == 1
                nx = x+dx[i]
                ny = y+dy[i]
                return check(ny,nx)
            else:
                print('4번')
                graph[y][x] == 1
                graph[y+1][x] == 1
                graph[y+2][x] == 1
                graph[y+2][x+1] == 1
                nx = x+dx[i]
                ny = y+dy[i]
                return check(ny,nx)
    
check(y,x)
count= 0
for i in graph:
    for j in i:
        if j == 1:
            count += 1
print(count)
    


