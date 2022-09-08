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
    



# for start in range(N-1):
#     #end = start + 1
#     while start < end:
#         summary = S[start] + S[end]
#         for end in range(start+1, N):
#             start2 = 0
#             end2 = N-1
#             summary = S[start] + S[end]
#             while start2 < end2:
#                 if start2 == end or start2 == start:
#                     start2 += 1
#                     continue
#                 elif end2 == end or end2 == start:
#                     end2 -= 1
#                     continue
#                 summary2 = S[start2] + S[end2]
#                 #print(summary, summary2, start, end, start2, end2)
#                 if min_v > abs(summary-summary2):
#                     min_v = abs(summary-summary2)
#                     if summary - abs(S[start2+1] + S[end2]) > summary - abs(S[start2] + S[end2-1]):
#                         end2 -= 1
#                     else:
#                         start2 += 1
#                 else:
#                     if summary - abs(S[start2+1] + S[end2]) > summary - abs(S[start2] + S[end2-1]):
#                         end2 -= 1
#                     else:
#                         start2 += 1

#print(min_v)
