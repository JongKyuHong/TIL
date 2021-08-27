n = int(input())
cnt = 0
for i in range(n,-1,-1):
    array = [n,i]
    while 1:
        a = array[-2]-array[-1]
        if a < 0:
            break
        else:
            array.append(a)
    if cnt < len(array):
        cnt = len(array)
        max_list = array
print(cnt)
print(*max_list)