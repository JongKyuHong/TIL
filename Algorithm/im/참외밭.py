k = int(input())

max_height = 0
max_width = 0
array = []
for i in range(6):
    a, b = map(int, input().split())
    if a == 1 or a == 2:
        if max_width < b:
            max_width = b
            w_idx = i
    else:
        if max_height < b:
            max_height = b
            h_idx = i
    array.append([a,b])
subw = abs(array[(w_idx - 1) % 6][1] - array[(w_idx + 1) % 6][1])
subh = abs(array[(h_idx - 1) % 6][1] - array[(h_idx + 1) % 6][1])

ans = ((max_width * max_height) - (subw* subh)) * k
print(ans)