
array = list(input())
stack = []
x = 0; cnt= 0
for i in range(len(array)):
    a = array.pop(0)
    if a == "(":
        x += 1; cnt += 1;
    else:
        if stack[-1] == "(":
            x -= 1; cnt-=1; cnt+=x
        else:
            x -= 1
    stack.append(a)
print(cnt)
