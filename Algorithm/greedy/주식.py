import sys

t = int(sys.stdin.readline())
result = []
for _ in range(t):
    n = int(sys.stdin.readline())
    stock = list(map(int,sys.stdin.readline().split()))
    stock.append(0)
    stocks = [0]*10001
    cnt = 0
    maximum = 0
    for i in range(len(stock)-1,-1,-1):
        if stock[i] > maximum:
            maximum = stock[i]
        elif stock[i] == maximum:
            continue
        else:
            cnt += maximum - stock[i]
    result.append(cnt)
for i in result:
    print(i)