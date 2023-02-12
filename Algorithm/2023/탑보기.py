import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
near = [[float('inf'),float('inf')] for _ in range(N+1)]
stack = []
cnt = [0]*(N+1)
for i in range(N):
    while stack and stack[-1][1] <= lst[i]:
        stack.pop()
    cnt[i] += len(stack)

    if stack:
        g = abs(stack[-1][0]-i)
        if g < near[i][1]:
            near[i][0] = stack[-1][0]
            near[i][1] = g
        elif g == near[i][1] and stack[-1][0] < near[i][0]:
            near[i][0] = stack[-1][0]
    stack.append([i, lst[i]])

stack = []
for i in range(N-1, -1, -1):
    while stack and stack[-1][1] <= lst[i]:
        stack.pop()
    cnt[i] += len(stack)

    if stack:
        g = abs(stack[-1][0]-i)
        if g < near[i][1]:
            near[i][0] = stack[-1][0]
            near[i][1] = g
        elif g == near[i][1] and stack[-1][0] < near[i][0]:
            near[i][0] = stack[-1][0]
    stack.append([i, lst[i]])

for i in range(N):
    if cnt[i] > 0:
        print(str(cnt[i]), str(near[i][0]+1))
    else:
        print(0)

