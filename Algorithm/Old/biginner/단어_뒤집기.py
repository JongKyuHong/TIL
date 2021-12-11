t = int(input())

for _ in range(t):
    n = list(input().split())
    for i in n:
        print(i[::-1], end=' ')


