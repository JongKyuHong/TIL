from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

n = int(input())
lst = [1,5,10,50]

A = list(combinations_with_replacement(lst, n))
answer = []
for a in A:
    if sum(a) not in answer:
        answer.append(sum(a))
print(len(answer))