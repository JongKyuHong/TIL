import sys
input = sys.stdin.readline

R,C,W = map(int, input().split())

triangle = [[1]*i for i in range(R+W)]

for i in range(2, R+W):
    for j in range(1,i-1):
        triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

# for i in triangle:
#     print(i)

cnt = 0
ans = 0
for i in range(R, R+W):
    cnt += 1
    for j in range(C-1,cnt+C-1):
        #print(i, j)
        ans += triangle[i][j]
print(ans)