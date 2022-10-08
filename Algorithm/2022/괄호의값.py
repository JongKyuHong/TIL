import sys
input = sys.stdin.readline

string = list(input().rstrip())
stack = []
answer = 0
ans = 1

for i in range(len(string)):
    if string[i] == '[':
       ans *= 3
       stack.append(string[i])
    elif string[i] == '(':
        ans *= 2
        stack.append(string[i])
    elif string[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if string[i-1] == '(':
            answer += ans
        stack.pop()
        ans //= 2
    elif string[i] == ']':
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if string[i-1] == '[':
            answer += ans
        stack.pop()
        ans //= 3

if not stack:
    print(answer)
else:
    print(0)