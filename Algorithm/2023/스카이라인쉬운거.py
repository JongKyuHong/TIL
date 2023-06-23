import sys
input = sys.stdin.readline

n = int(input())
stack = []
lst = []
for _ in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))
ans = 0
for i in lst:
    if stack:
        if stack[-1][1] < i[1]:
            ans += 1
            stack.append((i[0], i[1]))
        else:
            while stack and stack[-1][1] > i[1]:
                stack.pop()
            if i[1] == 0:
                continue
            if stack and stack[-1][1] == i[1]: # 스택값맨위랑 같은경우
                continue
            elif not stack or stack[-1][1] < i[1]:
                ans += 1
                stack.append((i[0],i[1]))
    else:
        if i[1] > 0:
            stack.append((i[0], i[1]))
            ans += 1
print(ans)