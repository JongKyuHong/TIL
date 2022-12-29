from itertools import combinations
import sys
input = sys.stdin.readline

words = list(input().rstrip())

lst = []
stack = []
for i in range(len(words)):
    if words[i] == '(':
        stack.append(i)
    elif words[i] == ')':
        idx = stack.pop()
        lst.append([idx, i])
answer = set()
for i in range(1, len(lst)+1):
    for combi in combinations(lst, i):
        tmp = words[:]
        for c in combi:
            start, end = c
            tmp[start] = ''
            tmp[end] = ''
        answer.add(''.join(tmp))

for c in sorted(answer):
    print(c)