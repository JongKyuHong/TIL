n = int(input())
words = [input() for _ in range(n)]
res = 0
for word in words:
    stack = []
    for w in word:
        if stack:
            if stack[-1] == w:
                stack.pop()
            else:
                stack.append(w)
        else:
            stack.append(w)
    if not stack:
        res += 1
    
print(res)