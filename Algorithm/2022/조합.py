def factorial(n):
    if n == 1:
        return 1
    num = n * factorial(n-1)
    return num

n, m = map(int, input().split())
res = 1
for i in range(m):
    res *= (n-i)
print(res//factorial(m))