stack = []
words = input()
target = input()
res = []
for i in words:
    stack.append(i)
    print(stack)
    if stack[-1] == target[-1]:
        for i in range(1,len(target)+1,1):
            if stack[-i] != target[-i]:
                for i in res:
                    stack.append(i)
                res = []
                break
            else:
                res.append(stack.pop())        
print(*stack)
            
    
    
            