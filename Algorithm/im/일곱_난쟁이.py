height = [int(input()) for _ in range(9)]
suma = sum(height)
res = []
flag = 0
for i in range(8):
    for j in range(i+1,9):
        if suma == 100 + (height[i]+height[j]):
            height.pop(i)
            height.pop(j-1)
            flag = 1
            break
    if flag == 1:
        break
height.sort()
for i in height:
    print(i)
