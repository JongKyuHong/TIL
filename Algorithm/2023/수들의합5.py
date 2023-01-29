import sys
input = sys.stdin.readline

N = int(input())
ans = 1
if N == 1:
    print(ans)
else:
    left, right = 1, 2
    sum_val = left
    while right <= N:
        if sum_val > N:
            sum_val -= left
            left += 1
        elif sum_val == N:
            ans += 1
            sum_val -= left
            left += 1
        else:
            sum_val += right
            right += 1
    print(ans)