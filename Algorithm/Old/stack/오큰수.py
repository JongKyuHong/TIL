n = int(input())
array = list(map(int,input().split()))
res = [-1]*n
stack = []  # 인덱스를 저장할 스택
stack.append(0)
for i in range(1,n):
    while stack and array[stack[-1]] < array[i]:
        res[stack.pop()] = array[i]
    stack.append(i)
print(*res)


