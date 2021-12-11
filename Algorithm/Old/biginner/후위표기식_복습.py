text = input()
stack = []
stack2 = []
for i in text:
    if i.isalpha():
        stack.append(i)
    elif i == ')' or i=='(':
        continue
    else:
        stack2.append(i)

print(''.join(stack),end='')
print(''.join(stack2[::-1]))