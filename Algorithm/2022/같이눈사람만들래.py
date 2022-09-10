import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
S.sort()
start = 0
#end = N-1
min_v = sys.maxsize
end = N-1
for start in range(N-3):
    for end in range(start+3, N):
        summary = S[start] + S[end]
        left, right = start+1, end-1
        while left < right:
            summary2 = S[left] + S[right]
            if abs(summary-summary2) < min_v:
                min_v = abs(summary-summary2)
            
            if summary2 < summary:
                left += 1
            elif summary2 > summary:
                right -= 1
            else:
                print(0)
                sys.exit(0)
print(min_v)
