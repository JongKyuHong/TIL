import sys 
input = sys.stdin.readline

T = int(input())

def cal(st):
    tmp = ''
    ops = []
    nums = []
    for i in st:
        if i.isdigit():
            tmp += i
        elif i == '+' or i == '-':
            ops.append(i)
            nums.append(tmp)
            tmp = ''
    nums.append(tmp)
    while ops:
        op = ops.pop(0)
        num1 = int(nums.pop(0))
        num2 = int(nums.pop(0))
        if op == '+':
            nums.insert(0, num1 + num2)
        else:
            nums.insert(0, num1 - num2)
    return nums[0]
def solve(num, st):
    global N, answer
    if num == N:
        if cal(st+str(N)) == 0:
            answer.append(st+str(N))
        return
    solve(num+1, st + str(num) +'+')
    solve(num+1, st + str(num) +'-')
    solve(num+1, st + str(num) + ' ')

for _ in range(T):
    N = int(input())
    answer = []
    solve(1, '')
    for i in sorted(answer):
        print(i)
    print()