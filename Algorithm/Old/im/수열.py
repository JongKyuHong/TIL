n, k = map(int, input().split())  # n은 온도를 측정한 전체 날짜의 수, k는 연속적인 날짜의 수
array = list(map(int, input().split()))
i = 0
tem_sum = sum(array[0:k])
max_sum = tem_sum
if k == 1:
    print(max(array))
else:
    while 1:
        tem_sum -= array[i]
        if i + k >= n:
            break
        tem_sum += array[i+k]
        if max_sum < tem_sum:
            max_sum = tem_sum
        i += 1
    print(max_sum)




