stack = []
n = list(input())
val = 0
for i in n:
    if not stack:
       stack.append(i)
       val += 10
    else:
        if stack[-1] == i:
            val += 5
        else:
            val += 10
        stack.append(i)
print(val)
