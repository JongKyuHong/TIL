import sys
input = sys.stdin.readline

N, K = map(int, input().split())
inp = input().rstrip()
stack = [inp[0]]
for i in range(1, N):
    while stack and K and stack[-1] < inp[i]:
        stack.pop()
        K -= 1
    stack.append(inp[i])
if K > 0:
    print(int(''.join(stack[:-K])))
else:
    print(int(''.join(stack)))
