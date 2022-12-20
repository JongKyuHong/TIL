import sys
input = sys.stdin.readline

N,m,M,T,R = map(int, input().split()) # N분, 초기맥박m, 넘으면안되는 맥박M, 운동시맥박증가T, 휴식시맥박감소R
state = m
if state + T > M:
    print(-1)
    exit()
e_time = 0
flag = 0
total_time = 0
while e_time < N:
    if state+T <= M:
        state += T
        e_time += 1
        total_time += 1
    else:
        state -= R
        if state < m:
            state = m
        total_time += 1
print(total_time)