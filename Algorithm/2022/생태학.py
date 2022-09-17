import sys
input = sys.stdin.readline

trees = dict()
cnt = 0
while 1:
    tree = input().rstrip()
    if not tree:
        break
    cnt += 1
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

res = []
for k, v in trees.items():
    v1 = v/cnt
    res.append((k, v1*100))

res.sort(key=lambda x : x[0])

for i in res:
    print(i[0],end=' ')
    print('{:.4f}'.format(i[1]))
