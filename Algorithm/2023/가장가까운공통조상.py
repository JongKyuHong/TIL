from collections import deque
import sys
input = sys.stdin.readline

def check(node):
    lst = [[node, 0]]
    visited = [0]*(N+1)
    visited[node] = 1
    q = deque()
    q.append([node, 0])
    while q:
        now, value = q.popleft()
        if not tree[now]:
            return sorted(lst, key=lambda x:x[1])
        for i in tree[now]:
            if not visited[i]:
                visited[i] = 1
                q.append([i,value+1])
                lst.append([i, value])

for _ in range(int(input())):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1):
        A, B = map(int, input().split())
        #tree[A].append(B)
        tree[B].append(A)
    A, B = map(int, input().split())
    a_lst, b_lst = check(A), check(B)
    flag = 0
    for a, v in a_lst:
        for b, vb in b_lst:
            if a == b:
                print(a)
                flag = 1
                break
        if flag:
            break