import sys
input = sys.stdin.readline

N = int(input())
lst = [float(input()) for _ in range(N)]

for i in range(1, N):
    lst[i] = max(lst[i-1]*lst[i], lst[i])
print(f'{max(lst):.3f}')