n = int(input())
array = list(map(int, input().split()))

num = array[0]
array.pop(0)
idx = 0
res = [num]
while array:
    idx = (idx+num)%len(array)
    res.append(idx)
    num = array[idx]
    array.pop(idx)

print(*res)