array = input()
stack = []
stack2 = []

n = len(array)
cnt = 0
for i in array:
    if i.isalpha():
        stack.append(i)
    elif i in ['*','+','-','/']:
        stack2.append(i)


print(''.join(stack),end='')
print(''.join(stack2[::-1]))