import sys
input = sys.stdin.readline

N = int(input())
xi = list(map(int, input().split()))
s = [0 for _ in range(N)]
val = sum(xi)
for i in range(N):
    s[i] = val
    val -= xi[i]
    
sum_v = 0
for i in range(N-1):
    sum_v += (xi[i]*s[i+1])

print(sum_v)