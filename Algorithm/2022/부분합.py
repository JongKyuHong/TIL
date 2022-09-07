import sys
input = sys.stdin.readline

N, S = map(int, input().split())
array = list(map(int, input().split()))
summary = 0
end = 0
len_ = 0
min_v = sys.maxsize
for start in range(N):
    while summary < S and end < N:
        summary += array[end] 
        len_ += 1
        end += 1
    print(summary, min_v, len_)
    # if summary < S:
    #     print(0)
    #     exit()
    if summary >= S:
        min_v = min(min_v, len_)
    summary -= array[start]
    len_ -= 1
print(min_v)
    
