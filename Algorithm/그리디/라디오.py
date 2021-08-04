def solution():
    min_value = 2e9
    for freq in frequency:
        min_value = min(min_value,abs(freq-B))
    return min(min_value+1,abs(A-B))

A,B = list(map(int,input().split()))
N = int(input())
frequency = [int(input()) for _ in range(N)]
answer = solution()
print(answer)