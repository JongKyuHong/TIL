import sys
input = sys.stdin.readline

n = int(input())
stack = []
nums = [int(input()) for _ in range(n)]
lst = [i for i in range(1, n+1)]
number = 1
idx = 0
answer = []
while idx < n and number <= n+1:
    #print(idx, number, stack, nums[idx])
    if stack and stack[-1] == nums[idx]:
        idx += 1
        answer.append('-')
        stack.pop()
    else:
        stack.append(number)
        number += 1
        answer.append('+')

if number >= n and idx < n:
    print('NO')
else:
    for i in answer:
        print(i)
