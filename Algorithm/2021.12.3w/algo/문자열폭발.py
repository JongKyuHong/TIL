stack = []
words = input()
target = input()
lasttarget = target[-1]
length_t = len(target)
for word in words:
    stack.append(word)
    if stack[-1] == target[-1] and ''.join(stack[-length_t:]) == target:
        del stack[-length_t:]
answer = ''.join(stack)
if answer == '':
    print('FRULA')
else:
    print(answer)