import sys
input = sys.stdin.readline

N = int(input())
product = []
for _ in range(N):
    C = int(input())
    product.append(C)
product.sort(reverse=True)
sum = 0
for i in range(N):
    if i % 3 != 2:
        sum += product[i]
print(sum)
