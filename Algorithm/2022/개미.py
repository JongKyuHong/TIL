import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split())
lst1 = list(input().rstrip())
lst2 = list(input().rstrip())
t = int(input())
target = lst1[::-1]+lst2

for _ in range(t):
    path = []
    for i in range(1, len(target)):
        if target[i] in lst2 and target[i-1] in lst1:
            path.append((i-1, i))
            #target[i-1], target[i] = target[i], target[i-1]
    for i, j in path:
        target[i], target[j] = target[j], target[i]

print(''.join(target))