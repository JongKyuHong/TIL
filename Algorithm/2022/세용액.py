import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

S.sort()
ans = []
min_v = sys.maxsize
flag = 0
for i in range(N-2):
    #target = -S[i]
    left = i+1
    right = N-1
    while left < right:
        summary = S[left] + S[right] + S[i]
        #print(S[i], S[left], S[right], min_v, summary)
        if summary == 0:
            ans = [S[i],S[left],S[right]]
            flag = 1
            break
        if abs(summary) < abs(min_v):
            min_v = summary
            ans = [S[i],S[left],S[right]]
            if summary < 0:
                left += 1
            else:
                right -= 1
        elif abs(summary) > abs(min_v):
            if summary < 0:
                left += 1
            else:
                right -= 1
        else:
            if summary < 0:
                left += 1
            else:
                right -= 1
            #left += 1
            #right -= 1

    if flag:
        break

print(*ans)