from itertools import permutations

def cal(num1, num2, op):
    if op == '+':
        return str(int(num1)+int(num2))
    if op == '-':
        return str(int(num1)-int(num2))
    if op == '*':
        return str(int(num1)*int(num2))

def calculate(exp, op):
    tmp = ''
    array = []
    for i in exp:
        if i.isdigit():
            tmp += i
        else:
            array.append(tmp)
            array.append(i)
            tmp = ''
    array.append(tmp)

    for i in op:
        stack = []
        while len(array) > 0:
            tmp = array.pop(0)
            if tmp != i:
                stack.append(tmp)
            else:
                stack.append(cal(stack.pop(), array.pop(0), i))
        array = stack
    print(array,'asdf')
    return abs(int(array[0]))


def solution(expression):
    op = ['+','-','*']
    op = list(permutations(op, 3))
    result = []
    for i in op:
        result.append(calculate(expression,i))
    return max(result)

print(solution("100-200*300-500+20"))
