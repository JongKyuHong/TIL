import sys
input = sys.stdin.readline

D, K = map(int, input().split())

if D == 3:
    print(1)
    print(K-1)
    exit()

left = 2; right = 1
left_day = D-2;right_day=D-3

while right_day > 1:
    after_left = left+right
    right = left
    left = after_left
    left_day -= 1
    right_day -= 1

for i in range(1, K): # 첫째날 떡
    for j in range(1, K): # 둘째날 떡
        if right*i + left*j == K:
            print(i)
            print(j)
            exit()