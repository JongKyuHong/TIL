from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = deque([i for i in range(1, N+1)])
nums = list(map(int, input().split()))
answer = 0
for num in nums:
    if numbers[0] != num:
        idx = numbers.index(num)
        if len(numbers) - idx > idx - 0: # 0에서 idx로 가는게 더 빠르다.
            while numbers[0] != num:
                numbers.append(numbers.popleft())
                answer += 1
        else:
            while numbers[0] != num:
                numbers.appendleft(numbers.pop())
                answer += 1
    numbers.popleft()
print(answer)