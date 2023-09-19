import sys 
input = sys.stdin.readline

class Node:
    def __init__(self, number, left_node, right_node):
        self.parent = -1
        self.number = number
        self.left_node = left_node
        self.right_node = right_node

def inorder(node, level):
    global level_depth, x
    level_depth = max(level_depth, level)
    if node.left_node != -1:
        inorder(tree[node.left_node], level+1)
    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)
    x += 1
    if node.right_node != -1:
        inorder(tree[node.right_node], level+1)

N = int(input())
tree = {}
level_min = [N]
level_max = [0]
root = -1
x = 1
level_depth = 1

for i in range(1, N+1):
    tree[i] = Node(i, -1, -1)
    level_min.append(N)
    level_max.append(0)

for _ in range(N):
    number, left, right = map(int, input().split())
    tree[number].left_node = left
    tree[number].right_node = right
    if left != -1:
        tree[left].parent = number
    if right != -1:
        tree[right].parent = number

for i in range(1, N+1):
    if tree[i].parent == -1:
        root = i
inorder(tree[root], 1)

result_level = 1
result_width = level_max[1] - level_min[1] + 1
for i in range(2, level_depth+1):
    width = level_max[i] - level_min[i] + 1
    if result_width < width:
        result_level = i
        result_width = width
print(result_level, result_width)