import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 
score = [0]*(n+1)
lst = []
for _ in range(n):
    res = sorted(list(map(int, input().split())),reverse=True)
    lst.append(res)

for i in range(m):
    max_v = 0
    max_v_res = []
    for j in range(n):
        if max_v < lst[j][i]:
            max_v = lst[j][i]
            max_v_res = [j]
        elif max_v == lst[j][i]:
            max_v_res.append(j)
        
    for v_res in max_v_res:
        score[v_res] += 1
max_score = max(score)
for i in range(n):
    if max_score == score[i]:
        print(i+1, end=' ')