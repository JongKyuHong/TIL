# import sys
# sys.stdin = open('input.txt')

for _ in range(1):
    tc, n = map(int,input().split())
    road = list(map(int,input().split()))

    # 1. 홀짝
    # 2. 2step
    # 3. 2*?
    for i in range(n):
        st = road[2*i]
        ed = road[2*i+1]
        print(st,ed)

    #########################
    # 저장 방법
    # 1. ch1, ch2
    ch1 = [0] * 100
    ch2 = [0] * 100

    for i in range(n):
        if ch1[road[2*i]] == 0:
            ch1[road[2*i]] = road[2*i+1]
        else:
            ch2[road[2*i]] = road[2*i+1]
    
    # 2. 인접행렬 방식
    adj_arr = [[0] * 100 for _ in range(100)]
    for i in range(n):
        adj_arr[road[2*i]][road[2*i+1]] = 1

    # 3. 인접리스트 방식
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        adj_list[road[2*i]].append(road[2*i+1])