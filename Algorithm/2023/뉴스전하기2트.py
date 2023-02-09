import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
child = [[] for _ in range(N+1)]
for i in range(1, N):
    child[lst[i]].append(i)
child_cnt = [0 for i in range(N+1)]
def find(node):
    child_node = []
    if len(child[node]) == 0:
        child_cnt[node] = 0
    else:
        for i in child[node]:
            find(i)
            child_node.append(child_cnt[i])
        child_node.sort(reverse=True)
        child_node = [child_node[i] + i + 1 for i in range(len(child_node))]
        child_cnt[node] = max(child_node)

find(0)
print(child_cnt[0])