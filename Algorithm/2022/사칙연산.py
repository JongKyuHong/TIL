for _ in range(int(input())):
    data = input().split()
    num1 = data[0]
    op = data[1]
    num2 = data[2]
    op2 = data[3]
    ans = data[4]
    if op == '+':
        if int(num1) + int(num2) == int(ans):
            print('correct')
        else:
            print('wrong answer')
    elif op == '-':
        if int(num1) - int(num2) == int(ans):
            print('correct')
        else:
            print('wrong answer')
    elif op == '*':
        if int(num1) * int(num2) == int(ans):
            print('correct')
        else:
            print('wrong answer')
    elif op == '/':
        if int(num1) / int(num2) == int(ans):
            print('correct')
        else:
            print('wrong answer')