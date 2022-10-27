import sys
input = sys.stdin.readline

a, b = 0, 0
res = []
for i in range(5):
    num = int(input())
    res.append(num)
res.sort()
print(sum(res)/len(res))
print(res[2])