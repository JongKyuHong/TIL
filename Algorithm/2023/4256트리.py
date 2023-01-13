import sys
input = sys.stdin.readline

def postorder(preorder, inorder):
    if len(preorder) == 0:
        return
    elif len(preorder) == 1:
        print(preorder[0], end=' ')
        return
    root_idx = inorder.index(preorder[0])
    left_in = inorder[:root_idx]
    left_pre = preorder[1:1+len(left_in)]
    postorder(left_pre, left_in)

    right_in = inorder[root_idx+1:]
    right_pre = preorder[len(left_pre)+1:]
    postorder(right_pre, right_in)
    print(preorder[0],end=' ')

    


for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    postorder(preorder, inorder)
    print()
