import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
ans = 0
for word in words:
    flag = 0
    check = {}
    stack = []
    for w in word:
        if w not in check:
            stack.append(w)
            check[w] = 1
        else:
            if stack[-1] == w:
                stack.append(w)
            else:
                flag = 1
                break
    if not flag:
        ans += 1
print(ans)