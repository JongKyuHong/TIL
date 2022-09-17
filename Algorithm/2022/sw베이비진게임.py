def babyjin(lst):
    for i in range(len(lst)):
        if lst[i] == 3:
            return 2 # 트리플렛
        if i == 0:
            if lst[i] and lst[i+1] and lst[i+2]:
                return 1
        elif i == len(lst)-1:
            if lst[i-2] and lst[i-1] and lst[i]:
                return 1
        else:
            if lst[i-1] and lst[i] and lst[i+1]:
                return 1
    return 0

for T in range(int(input())):
    nums = list(input().split())
    A = [0] * 10
    B = [0] * 10
    res = 0
    for i in range(12):
        if i % 2:
            B[int(nums[i])] += 1
            if i >= 5:
                b = babyjin(B)
                if b:
                    res = 2
                    break
        else:
            A[int(nums[i])] += 1
            if i >= 4:
                a = babyjin(A)
                if a:
                    res = 1
                    break
           
    print(f'#{T+1} {res}')