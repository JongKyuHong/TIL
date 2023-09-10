import sys 
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append([x, y])
for tmp in sorted(lst, key=lambda x: (x[0], x[1])):
    print(*tmp)