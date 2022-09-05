S = input()
s= ''
for i in S:
    if i.isalpha():
        s += i
k = input()
if k in s:
    print(1)
else:
    print(0)