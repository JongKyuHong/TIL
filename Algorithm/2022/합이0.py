import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

S.sort()
ans = 0
for i in range(N-2):
    left, right = i+1, N-1
    goal = -S[i]
    mx_idx = N
    while left < right:
        tmp = S[left] + S[right]
        if tmp < goal:
            left += 1
        elif tmp == goal:
            if S[left] == S[right]:
                ans += right - left
            else:
                if mx_idx > right:
                    mx_idx = right
                    while mx_idx >= 0 and S[mx_idx - 1] == S[right]:
                        mx_idx -= 1
                ans += right-mx_idx + 1
            left += 1
        else:
            right -= 1
print(ans)
    


# while start < N-2: # 당연히 실패
#     while mid < N-1:
#         while end < N:
#             summary = S[start] + S[mid] + S[end]
#             #print(summary)
#             if summary == 0:
#                 cnt += 1
#                 end += 1
#             elif summary < 0:
#                 end += 1
#             else:
#                 break
#         mid += 1
#         end = mid + 1
#     start += 1
#     mid = start + 1

#print(cnt)
    