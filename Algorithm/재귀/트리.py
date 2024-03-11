import sys
input = sys.stdin.readline

def buildTree(preorder, inorder):
    if len(preorder) == 0:
        return
    elif len(preorder) == 1:
        _tree.append(preorder[0])
        return

    root_val = preorder[0]
    root_index = inorder.index(root_val)

    buildTree(preorder[1:root_index+1], inorder[:root_index])
    buildTree(preorder[root_index+1:], inorder[root_index+1:])
    _tree.append(root_val)

T = int(input())
for _ in range(T):
    n = int(input())
    _tree = []
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    
    buildTree(preorder, inorder)
    print(*_tree)

