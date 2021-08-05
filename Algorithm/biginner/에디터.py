text = list(input())
text2 = []
m = int(input())

for _ in range(m):
    a = input().split()
    if a[0] == 'P':
        text.append(a[1])
    elif a[0] == 'L':
        if text: text2.append(text.pop())
    elif a[0] == 'D':
        if text2: text.append(text2.pop())
    elif a[0] == 'B':
        if text: text.pop()
        else: continue
print(''.join(text+list(reversed(text2))))




