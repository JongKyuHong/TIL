import sys 
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    cnt = 0
    for a in range(1, n): # a
        for b in range(a+1, n): # b
            if (a**2 + b**2 + m)/(a*b) == int((a**2 + b**2 + m)/(a*b)):
                cnt += 1
    print(cnt)
 