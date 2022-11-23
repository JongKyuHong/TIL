import sys
input = sys.stdin.readline

cows = input().rstrip()
lst = [[-1, -1] for _ in range(26)]

for i in range(52):
    if lst[ord(cows[i])-65][0] == -1:
        lst[ord(cows[i])-65][0] = i
    else:
        lst[ord(cows[i])-65][1] = i
ans = 0
for i in range(26):
    for j in range(26):
        r1, c1, r2, c2 = lst[i][0], lst[i][1], lst[j][0], lst[j][1]
        if r1 < r2 and r2 < c1 and c1 < c2:
            ans += 1

print(ans)