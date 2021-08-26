a = int(input())
array = list(map(int,input().split()))

stack = []
stack.append(0)
res = [-1] * a
for i in range(1,a):
    while stack and array[stack[-1]] < array[i]:
        res[stack.pop()] = array[i]
    stack.append(i)
print(*res)