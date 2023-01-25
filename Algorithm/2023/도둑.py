import sys
input = sys.stdin.readline

for _ in range(int(input())):   
    N, M, K = map(int, input().split()) # 집의갯수, 연속된 집의개수, 최소 돈의 양
    house = list(map(int, input().split()))
    house += house[:M-1]
    S = [0]*N
    S[0] = sum(house[:M])
    val = 0
    if S[0] < K:
        val += 1
    if N == M:
        print(val)
        continue
        
    for i in range(1, N):
        S[i] = S[i-1] - house[i-1] + house[i+M-1]
        if S[i] < K:
            val += 1
    print(val)
