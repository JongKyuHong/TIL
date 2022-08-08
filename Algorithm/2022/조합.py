from itertools import combinations

n, m = map(int, input().split())

listn = list(range(1, n+1))

combi = len(list(combinations(listn,6)))
print(combi)