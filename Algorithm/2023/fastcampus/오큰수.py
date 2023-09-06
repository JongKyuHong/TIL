import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
stack = []
answer = [-1]*N
for i in range(N):
    num = nums[i]
    if not stack or stack[-1][0] >= num:
        stack.append((nums[i], i))
    else:
        while len(stack) > 0:
            previous, index = stack.pop()
            if previous >= num:
                stack.append((previous, index))
                break
            else:
                answer[index] = num
        stack.append((num, i))


print(*answer)