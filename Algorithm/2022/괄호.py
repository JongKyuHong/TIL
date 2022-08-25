import sys
input = sys.stdin.readline
for _ in range(int(input())):
    stack = []
    data = input().rstrip()
    flag = 0
    for i in data:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                flag = 1
                break

    if flag:
        print('NO')
    else:
        if stack:
            print("NO")
        else:
            print('YES')