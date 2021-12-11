n, m = map(int, input().split())  # 가로길이 세로길이

x_list = [0, n]
y_list = [0, m]
for _ in range(int(input())):
    c, r = map(int, input().split())
    if c == 0:
        y_list.append(r)
    else:
        x_list.append(r)

x_list.sort()
y_list.sort()
max_square = 0
for i in range(1, len(x_list)):
    for j in range(1, len(y_list)):
        width = x_list[i] - x_list[i-1]
        height = y_list[j] - y_list[j-1]
        max_square = max(max_square, width * height)
print(max_square)