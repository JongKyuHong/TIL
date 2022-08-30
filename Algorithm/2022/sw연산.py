from collections import deque

def bfs():
    global res
    while q:
        num, cnt = q.popleft()
        if num == m:
            res = min(res, cnt)
            return
        for i in range(4):
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

            else:
                num2 = num - 10
                if 0 < num2 <= 1000000 and numbers[num2] != 1:
                    q.append((num2, cnt+1))
                    numbers[num2] = 1

for T in range(int(input())):
    numbers = [0] * 1000001
    n, m = map(int, input().split())
    q = deque()
    q.append((n, 0))
    numbers[n] = 1
    res = float('inf')
    bfs()
    print(f'#{T+1} {res}')
    