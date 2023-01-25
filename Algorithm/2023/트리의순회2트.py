import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
inorder = list(map(int, input().split())) # 루트가 센터에
postorder = list(map(int, input().split())) # 루트가 뒤에
def maketree(instart, inend, poststart, postend):
    if (instart > inend) or (poststart > postend):
        return
    root = postorder[postend]
    
    left = nodeNum[root] - instart
    right = inend - nodeNum[root]
    print(root, end=' ')
    maketree(instart, instart+left-1, poststart, poststart+left-1)
    maketree(inend-right+1, inend, postend-right, postend-1)

nodeNum = [0] * (n + 1)
for i in range(n):
    nodeNum[inorder[i]] = i
maketree(0, n-1, 0, n-1)