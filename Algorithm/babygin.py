n = int(input())
for _ in range(n):
    array = list(map(int,input()))
    count_array = [0]*10
    for i in range(len(array)):
        count_array[array[i]] += 1
    cnt = 0 # triple
    cnt2 = 0 # run
    i = 0
    while i < 10:
        if count_array[i] >= 3:
            count_array[i] -= 3
            cnt += 1
            continue            
        if count_array[i] >= 1 and count_array[i+1] >= 1 and count_array[i+2]>=1:
            count_array[i] -= 1
            count_array[i+1] -= 1
            count_array[i+2] -= 1
            cnt2 += 1
            continue
        i += 1
    if cnt + cnt2 == 2:
        print('baby-gin')




