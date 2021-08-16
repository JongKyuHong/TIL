import sys

S = sys.stdin.readline()
new = ''
for i in S:
    if i.isupper():
        if ord(i)+13 > ord('Z'):
            new += chr(ord(i)-13)
        else:
            new += chr(ord(i)+13)
    elif i.islower():
        if ord(i)+13 > ord('z'):
            new += chr(ord(i)-13)
        else:
            new += chr(ord(i)+13)
    elif i.isspace():
        new += ' '
    else:
        new += i
print(new)

