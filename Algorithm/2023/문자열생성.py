import sys
input = sys.stdin.readline

N = int(input())
S = ''
for _ in range(N):
    S += input().rstrip()
T = ''
left, right = 0, N-1
while left < right:
    if S[left] > S[right]:
        T += S[right]
        right -= 1
    elif S[left] < S[right]:
        T += S[left]
        left += 1
    else:
        l, r = left+1, right-1
        while l < r:
            if S[l] > S[r]:
                T += S[right]
                right -=1
                break
            elif S[l] < S[r]:
                T += S[left]
                left += 1
                break
            else:
                l += 1
                r -= 1
        else:
            T += S[left]
            left += 1
    if len(T) == 80:
        print(T)
        T = ''
T += S[left]
print(T)
    

