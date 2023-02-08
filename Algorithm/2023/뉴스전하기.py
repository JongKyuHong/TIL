from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
child = [[] for i in range(N)]
for i in range(1, N):
    child[lst[i]].append(i)

child_cnt = [0 for _ in range(N)]

def find(idx):
    child_node = []
    if len(child[idx]) == 0:
        child_cnt[idx] = 0
    else:
        for i in child[idx]:
            find(i)
            child_node.append(child_cnt[i])
        child_node.sort(reverse=True)
        child_node = [child_node[i] + i + 1 for i in range(len(child_node))]
        child_cnt[idx] = max(child_node)

find(0)
print(child_cnt[0])