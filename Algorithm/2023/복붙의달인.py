import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s, p = input().rstrip().split()
    while p in s:
        s = s.replace(p, '1')
    print(len(s))
            

