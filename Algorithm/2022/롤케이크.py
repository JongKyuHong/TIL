import sys
input = sys.stdin.readline

L = int(input())
N = int(input())
cake = [0]*(L+1)
take = [0]*N
longest = 0
longest_p = 0
for j in range(N):
    p, k = map(int, input().split())
    if k-p > longest:
        longest = k-p
        longest_p = j
    for i in range(p, k+1):
        if cake[i] == 0:
            cake[i] = 1
            take[j] += 1
print(longest_p+1)
longest_p = 0
longest = 0
for i in range(N):
    if take[i] > longest:
        longest = take[i]
        longest_p = i
print(longest_p+1)
        
