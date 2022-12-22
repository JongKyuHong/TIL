import sys
input = sys.stdin.readline

n = int(input())
lst = list(input().rstrip())
dp = [float('inf')]*n
dp[0] = 0
B, O, J = [], [], []
for i in range(n):
    if lst[i] == 'B':
        B.append(i)
    elif lst[i] == 'O':
        O.append(i)
    else:
        J.append(i)
idx = 0
flag = 0
while idx < n:
    if lst[idx] == 'B':
        for i in O:
            if not flag:
                plus = i
                flag = 1
            if i > idx:
                dp[i] = min(dp[i], (i-idx)**2+dp[idx])        
    elif lst[idx] == 'O':
        for i in J:
            if i > idx:
                dp[i] = min(dp[i], (i-idx)**2+dp[idx])
    else:
        for i in B:
            if i > idx:
                dp[i] = min(dp[i], (i-idx)**2+dp[idx])
    if flag == 1:
        idx += plus
        flag += 1
    else:
        idx += 1

print(dp[n-1] if dp[n-1] != float('inf') else -1)