from collections import defaultdict
import sys 
input = sys.stdin.readline

R, C, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
time = 0
while 1:

    if len(A) >= R and len(A[0]) >= C and A[R-1][C-1] == K:
        print(time)
        break
    elif time > 100:
        print(-1)
        break
    N = len(A)
    M = len(A[0])
    if N >= M: # 행이 더 큰 경우
        max_v = 0
        for i in range(N):
            dic = defaultdict(int)
            for j in range(M):
                if A[i][j] != 0:
                    dic[A[i][j]] += 1
            dic = sorted(dic.items(), key=lambda x: (x[1],x[0]))
            tmp = []
            for k, v in dic:
                tmp.append(k)
                tmp.append(v)
            A[i] = tmp
            max_v = max(max_v, len(tmp))
        
        for i in range(N):
            if len(A[i]) < max_v:
                for _ in range(max_v - len(A[i])):
                    A[i].append(0)
    else: # 열이 더 큰 경우
        tmp = []
        max_v = 0
        for i in range(M):
            dic = defaultdict(int)
            for j in range(N):
                if A[j][i] != 0:
                    dic[A[j][i]] += 1
            dic = sorted(dic.items(), key=lambda x: (x[1], x[0]))
            tmp2 = []
            for k, v in dic:
                tmp2.append(k)
                tmp2.append(v)
            max_v = max(max_v, len(tmp2))
            tmp.append(tmp2)

        for i in range(len(tmp)):
            if len(tmp[i]) < max_v:
                for _ in range(max_v - len(tmp[i])):
                    tmp[i].append(0)

        tmp3 = []
        for i in range(len(tmp[0])):
            tmp4 = []
            for j in range(len(tmp)):
                tmp4.append(tmp[j][i])
            tmp3.append(tmp4)
        A = tmp3
    time += 1
    # print('---------')
    # for i in A:
    #     print(i)
    # print('---------')
# 행의 개수가 같거나 크면 계수정렬을 행으로 수행
# 열의 개수가 크면 열로 진행
# A[r][c]에 들어있는값이 k가 되기 위한 최소 시간을 구하라