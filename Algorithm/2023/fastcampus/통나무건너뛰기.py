import sys 
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    left, right = [], []
    L.sort()
    for i in range(N):
        if i % 2:
            right.append(L[i])
        else:
            left.append(L[i])
    right.reverse()
    result = left + right
    answer = 0
    for i in range(N):
        if i == N-1:
            tmp = abs(result[N-1] - result[0])
        else:
            tmp = abs(result[i] - result[i+1])
        answer = max(answer, tmp)
    print(answer)
    # 가장 차이가 많이나는곳을 가장 작게해서 출력하라
    # 내 생각
    # 일단 L을 정렬함
    # left, right 리스트를 만든다
    # L에서 left하나 right하나씩 값을 넣음
    # left 값과 right값을 뒤집어서 합침
    # 걔중에서 차이가 가장 큰곳 찾기



