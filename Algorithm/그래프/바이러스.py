n = int(input())


def dfs(index):
    global cnt
    visited[index] = 1
    for i in nodes[index]:
        if not visited[i]:
            dfs(i)
            cnt += 1
        

linked_computer = int(input())
nodes = [[]*n for _ in range(n+1)]
for i in range(linked_computer):
    parent, child = map(int, input().split())
    nodes[parent].append(child)
    nodes[child].append(parent)

cnt = 0
visited = [0]*(n+1)
dfs(1)
print(cnt)
