import sys
sys.stdin = open('input.txt')

a = list(input())
stack = []
res = []
icp = {'*':2, '/' : 2,'+' :1  ,'-':1}
for i in a:
    if i.isdigit():
        res.append(i)
    else:
        while stack:
            if icp.get(i) > icp.get(stack[-1]):
                break
            res.append(stack.pop())
        stack.append(i)
while stack:
    res.append(stack.pop())

print(''.join(res))



