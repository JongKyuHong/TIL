import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

cnt = 0
def cnt_(node):



def find(root):
    global cnt
    if root == -1:
        return
    left, right = graph[root][0][0], graph[root][0][1]
    if left != -1:
        cnt_(left)
    cnt_(root)
    if right != -1:
        cnt_(right)

find(1)
print(cnt)