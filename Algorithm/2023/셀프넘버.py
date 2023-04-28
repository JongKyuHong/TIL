import sys
input = sys.stdin.readline

def find(num):
    num_str = str(num)
    tmp = num
    for i in num_str:
        tmp += int(i)
    if tmp > 10000:
        return
    dp[tmp] = 1
    find(tmp)

dp = [0]*10001
num = 1
for i in range(1, 10001):
    if dp[i]:
        continue
    else:
        find(i)
for i in range(1, 10001):
    if not dp[i]:
        print(i)    