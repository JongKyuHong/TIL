import sys
input = sys.stdin.readline

string = input().rstrip()
devil = input().rstrip()
angel = input().rstrip()

dp = [[[0]*2 for _ in range(101)] for _ in range(len(string))]
# 0이 천사
# 1이 악마
ans = 0
for i in range(len(devil)):
    if string[0] == devil[i]:
        dp[0][i][1] = 1
    if string[0] == angel[i]:
        dp[0][i][0] = 1

ans = 0
for i in range(len(devil)):
    for j in range(len(string)):
        if dp[j][i][0]:
            if j == len(string)-1:
                ans += dp[j][i][0]
            else:
                for k in range(i+1, len(devil)):
                    if devil[k] == string[j+1]:
                        dp[j+1][k][1] += dp[j][i][0]
        if dp[j][i][1]:
            if j == len(string)-1:
                ans += dp[j][i][1]
            else:
                for k in range(i+1, len(devil)):
                    if angel[k] == string[j+1]:
                        dp[j+1][k][0] += dp[j][i][1]
print(ans)
# 일단 string의 첫번째 와 같은 문자를 찾음
# 그다음에 순회를 하는데
# 두번째 문자와 같은 문자를 찾으면?




    



