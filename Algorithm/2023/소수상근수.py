import sys
input = sys.stdin.readline

nums = [0, 0] + [1] * 999999
for i in range(2, 1000001):
    if nums[i]:
        for j in range(i**2, 1000001, i):
            nums[j] = 0

n = int(input())
for i in range(2, n):
    if nums[i]: # 소수 이면서
        tmp_value = str(i)
        flag = 0
        val = []
        while 1:
            tmp = 0
            for j in tmp_value: # 상근수 판별
                tmp += int(j)**2
            if tmp == 1:
                print(i)
                break
            if tmp in val:
                break
            tmp_value = str(tmp)
            val.append(tmp)
