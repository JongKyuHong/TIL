
for _ in range(1,11):
    tc = int(input())
    array = [list(map(int,input().split())) for _ in range(100)]
    x,y = array[99].index(2), 99  # 도착지점을 먼저 찾음
    
    while 1:  # 무한루프
        if x>0 and array[y][x-1]:  # x가 0보다 크고 바로왼쪽이 0이 아닌경우 즉, 왼쪽으로 갈 수 있는경우
            while x>0 and array[y][x-1]:  # 한번에 여러칸 보내기위해 while문
                x -= 1
            else:  # 만약에 더이상 전진못하면
                y -= 1  # y값증가
        elif x<99 and array[y][x+1]:
            while x < 99 and array[y][x+1]:
                x += 1
            else:
                y -= 1
        else:
            y -= 1
        if y == 0:
            break
    print(f'#{tc} {x}')

    



