from collections import deque


def calculation(n):
    que = deque([(n, 0)])
    #que.append()
    while que:
        n, cnt = que.popleft()
        for i in range(4):
            if i == 0:
                n1 = n + 1
            elif i == 1:
                n1 = n - 1
            elif i == 2:
                n1 = n * 2
            else:
                n1 = n - 10
            if n1 == m:
                return cnt + 1
            elif 0 < n1 <= 10**6 and count_list[n1] != 1:
                que.append((n1, cnt+1))
                count_list[n1] = 1


for test_case in range(int(input())):
    n, m = map(int, input().split())
    #cal = [+1,-1,*2,-10]
    count_list = [0]*((10**6)+1)
    cnt = calculation(n)
    print(f'#{test_case+1} {cnt}')
    



