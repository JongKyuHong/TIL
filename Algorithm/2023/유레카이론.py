import sys
input = sys.stdin.readline

T = int(input())
nums = [i*(i+1) // 2 for i in range(1, 46)]
lst = [0]*1001
for i in nums:
    for j in nums:
        for k in nums:
            tmp = i+j+k
            if tmp <= 1000:
                lst[tmp] = 1
for _ in range(T):
    K = int(input()) #     
    print(lst[K])


