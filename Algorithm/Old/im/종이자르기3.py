w, h = map(int, input().split())  # 가로, 세로
k = int(input())  # 칼로 잘라야하는 점선의 갯수
x_list = [0, w]
y_list = [0, h]
for _ in range(k):
    a, b = map(int, input().split())
    if a == 0:
        y_list.append(b)
    else:
        x_list.append(b)
x_list.sort()
y_list.sort()
max_square = 0
for i in range(1, len(x_list)):
    for j in range(1, len(y_list)):
        width = x_list[i] - x_list[i-1]
        height = y_list[j] - y_list[j-1]
        max_square = max(max_square, width * height)
print(max_square)
    
