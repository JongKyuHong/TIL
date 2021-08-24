def check(arr,index):
    if index > 1:
        if arr[index-2] and arr[index-1]:
            return True
    if index < len(arr)-3:
        if arr[index+2] and arr[index+1]:
            return True
    if 0 < index < len(arr)-2:
        if arr[index+1] and arr[index-1]:
            return True
    return False
    


for test_case in range(int(input())):
    number = list(map(int,input().split()))
    # a1 = number[0:len(number):2]
    # a2 = number[1:len(number):2]
    a1_cnt = [0]*len(number)
    a2_cnt = [0]*len(number)
    winner = 0
    for i in range(12):
        if i%2:
            a2_cnt[number[i]] += 1
            if a2_cnt[number[i]] == 3 or check(a2_cnt,number[i]):
                winner = 2
        else:
            a1_cnt[number[i]] += 1
            if a1_cnt[number[i]] == 3 or check(a1_cnt,number[i]):
                winner = 1
    print(f'#{test_case+1} {winner}')