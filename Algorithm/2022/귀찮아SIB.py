import sys
input = sys.stdin.readline

n = int(input())
xi = list(map(int, input().split()))
sum_arr = [0] * (n-1)
target = sum(xi) - xi[0]
for i in range(n-1):
    sum_arr[i] = target*xi[i]
    target -= xi[i+1]
print(sum_arr)
