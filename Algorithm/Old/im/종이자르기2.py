width, height = map(int, input().split())
n = int(input())
list_1 = [0, width]  # 세로자를때
list_0 = [0, height]  # 가로자를때
for _ in range(n):
    a, b = map(int, input().split())
    if a == 0:  # 가로자르면
        list_0.append(b)
    else:  # 세로 자르면
        list_1.append(b)
list_0.sort()
list_1.sort()
max_square = 0
for i in range(1, len(list_1)):  # 가로 자르고 
    for j in range(1, len(list_0)):  # 세로 자르고
        width = list_1[i] - list_1[i-1]
        height = list_0[j] - list_0[j-1]
        max_square = max(width*height, max_square)
print(max_square)
