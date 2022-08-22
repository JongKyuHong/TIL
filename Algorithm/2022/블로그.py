N, X = map(int, input().split())
array = list(map(int, input().split()))

if max(array) == 0:
    print('SAD')
    exit()
value = sum(array[:X])
left, right = 0, N-1
max_v = value
max_cnt = 1

for i in range(X,N):
    value += array[i]
    value -= array[i-X]

    if value > max_v:
        max_v = value
        max_cnt = 1
    elif value == max_v:
        max_cnt += 1
print(max_v)
print(max_cnt)