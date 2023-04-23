import sys
input = sys.stdin.readline

S = input().rstrip()
M = int(input())
dp = [0] * (len(S)+1)
word = []
for _ in range(M):
    A, X = input().rstrip().split()
    word.append([A, X])

for i in range(1,len(S)+1):
    for j in range(M):
        if i >= len(word[j][0]) and S[i-len(word[j][0]):i] == word[j][0]:
            dp[i] = max(dp[i], dp[i-len(word[j][0])]+ int(word[j][1]))
    dp[i] = max(dp[i-1]+1, dp[i])

print(dp[-1])