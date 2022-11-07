import sys 
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
ans = len(A)
A = set(A)
res = len(A)
print(ans-res)