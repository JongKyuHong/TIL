from itertools import product
import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 자연수N, 집합K
arr = list(map(str, input().split())) # k의 원소들
length = len(str(n))

while 1:
    temp = list(product(arr, repeat=length))
    ex = []
    for i in temp:
        now = int(''.join(i))
        if now <= n:
            ex.append(now)
    if len(ex) >= 1:
        print(max(ex))
        break
    else:
        length -= 1
