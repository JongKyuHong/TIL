from collections import deque
import sys 
input = sys.stdin.readline

N, K = map(int, input().split())
lst = deque(list(map(int, input().split())))
lst2 = deque([0]*(2*N))

# 1. 벨트가 한칸 회전
# 2. 가장 먼저 올라간 로봇부터 움직일 수 있으면 움직인다. 이동할 수 없으면 가만히
# 3. 내구도가 0이 아니면 로봇하나더 올리기
# 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료

answer = 1
i = 1
while 1:
    lst.rotate(1)
    lst2.rotate(1)

    if lst2[N-1]:
        lst2[N-1] = 0

    for i in range(N-1, 0, -1):
        if lst[i] > 0 and lst2[i] == 0 and lst2[i-1]:
            lst[i] = lst[i] - 1
            lst2[i] = lst2[i-1]
            lst2[i-1] = 0

    if lst2[N-1]:
        lst2[N-1] = 0

    if lst[0] > 0:
        lst[0] = lst[0] - 1
        lst2[0] = i
        i += 1

    if lst.count(0) >= K:
        print(answer)
        exit()
    answer += 1