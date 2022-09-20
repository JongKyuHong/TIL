from collections import deque

def check(a):
    stack = []
    for i in a:
        if i == '(':
            stack.append(i)
        elif i == '{':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
    if stack:
        return 0
    else:
        return 1
        
def solution(s):
    answer = -1
    s = deque(list(s))
    len_s = len(s)
    cnt = check(s)
    for _ in range(len_s-1):
        target = s.popleft()
        s.append(target)
        cnt += check(s)

    return cnt

print(solution("}}}"))