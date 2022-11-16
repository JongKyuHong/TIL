from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

res = []
idx = 1
for i in lst:
    target = list(combinations(i, 3))
    answer = 0
    for t in target:
        answer_jj = 0
        for j in t:
            answer_jj += j
        answer = max(int(str(answer)[-1]), int(str(answer_jj)[-1]))
    res.append([answer, idx])
    idx += 1

res.sort(key=lambda x:(x[0],x[1]), reverse=True)
print(res[0][1])