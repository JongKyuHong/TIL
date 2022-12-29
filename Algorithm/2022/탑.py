import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
ans = []
stack = []
for i in range(N):
    while stack:
        if stack[-1][1] > towers[i]:
            ans.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    if not stack:
        ans.append(0)
    stack.append([i, towers[i]])
print(' '.join(map(str, ans)))