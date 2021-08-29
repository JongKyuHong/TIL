width, height = map(int, input().split())  # 블록의 가로와 세로
shops = int(input())  # 상점 갯수
array = []
sum_distance = 0
round = (width + height)*2  # 둘레
for _ in range(shops+1):
    a, b = map(int, input().split())  # 사방향중 위치, 위치에대한 값?
    if a == 1:  # 북쪽이야
        distance = b  # 그냥 일자로
    elif a == 2:  # 남쪽이야
        distance = width + height + width - b
    elif a == 3:  # 서쪽이야
        distance = width + height + width + height - b
    else:  # 동쪽이야
        distance = width + b
    array.append([a, b, distance])

dong = array[-1]
dong_dis = array[-1][-1]
for i in range(shops):
    a, b, distance = array[i]
    clockwise = abs(dong_dis - distance)
    sum_distance += min(clockwise, round-clockwise)
print(sum_distance)





