from itertools import combinations
import sys
input = sys.stdin.readline

inp = list(input().rstrip())
lst, lst2 = [], []
for i in range(len(inp)):
    if inp[i] == '(':
        lst2.append(i)
    elif inp[i] == ')':
        lst.append((lst2.pop(),i))
answer = set()
for i in range(1, len(lst)+1):
    for combi in combinations(lst, i):
        tmp = inp[:]
        for c in combi:
            start, end = c
            tmp[start] = ''
            tmp[end] = ''
        answer.add(''.join(tmp))

for c in sorted(answer):
    print(c)