import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs():
    global start_num, end_num, result, tc
    while q:
        num, cnt = q.popleft()
        if num == end_num:
            result = cnt
            return

        for i in range(4):
            num2 = 0
            if i == 0:
                num2 = num + 1
                if 0 < num2 <= 1000000 and numbers[num2] != 1:
                    q.append((num2, cnt+1))
                    numbers[num2] = 1

            elif i == 1:
                num2 = num - 1
                if 0 < num2 <= 1000000 and numbers[num2] != 1:
                    q.append((num2, cnt+1))
                    numbers[num2] = 1

            elif i == 2:
                num2 = num*2
                if 0 < num2 <= 1000000 and numbers[num2] != 1:
                    q.append((num2, cnt+1))
                    numbers[num2] = 1

            elif i == 3:
                num2 = num - 10
                if 0 < num2 <= 1000000 and numbers[num2] != 1:
                    q.append((num2, cnt+1))
                    numbers[num2] = 1


for test_case in range(int(input())):
    numbers = [0] * 1000001
    start_num, end_num = map(int, input().split())
    q = deque()
    q.append((start_num, 0))
    numbers[start_num] = 1
    result = 0
    bfs()
    print(f'#{test_case+1} {result}')