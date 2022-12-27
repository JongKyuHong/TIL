from itertools import combinations
import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 선을 그은 횟수
words = [input().rstrip() for _ in range(n)]
if k < 5:
    print(0)
    exit()

tmp2 = 'bdefghjklmopqrsuvwxyz'
res = 0
for c in combinations(tmp2, k-5):
    tmp = 'antic'
    ans = 0
    for j in c:
        if j not in tmp:
            tmp += j
    
    for i in range(n):
        flag = 0
        for j in range(4, len(words[i])-3):
            if words[i][j] not in tmp:
                flag = 1
                break
        if not flag:
            ans += 1
    res = max(res, ans)
print(res)