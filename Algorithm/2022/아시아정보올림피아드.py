import sys 
input = sys.stdin.readline

n = int(input())
res = []
for _ in range(n):
    a, b, c = map(int, input().split())
    res.append((a,b,c))

res.sort(key=lambda x:x[2], reverse=True)
ans = []
idx = 0
for i in res:
    if ans.count(i[0]) < 2 and idx < 3:
        print(i[0], i[1])  
        ans.append(i[0])
        idx += 1
    else:
        continue 