import sys
input = sys.stdin.readline

n, W = map(int, input().split())
price = []
num = 0
for _ in range(n):
    price.append(int(input()))
for i in range(n-1):
    if price[i] < price[i+1]:
        if W // price[i] > 0:
            num = W//price[i]
            W = W-(num*price[i])
    elif price[i] > price[i-1]:
        W += num*price[i]
        num = 0
if num > 0:
    W += num*price[-1]
print(W)
