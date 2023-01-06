import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
stack = [[towers[0],0]]
ans = [0]

for i in range(1, N):
    if stack[-1][0] < towers[i]:
        while stack and stack[-1][0] < towers[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1][1]+1)
        else:
            ans.append(0)
        stack.append([towers[i], i])
    else:
        ans.append(stack[-1][1]+1)
        stack.append([towers[i],i])
print(*ans)