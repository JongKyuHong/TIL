import sys 
input = sys.stdin.readline

def solution(arr):
    visited = [0]*N
    tmp = arr[0]
    idx = 1
    # print()
    # print(arr,'arr')
    # print()
    while idx < N:
        if tmp > arr[idx]:
            if tmp - 1 == arr[idx]:
                if idx + L > N:
                    return False
                else:
                    for j in range(idx, idx+L): # L앞까지 
                        if arr[j] != arr[idx] or visited[j] == 1:
                            return False
                    for j in range(idx, idx+L):
                        visited[j] = 1
                    idx += (L-1)
            else:
                return False
        elif tmp < arr[idx]: # tmp가 더 작은 경우
            if tmp + 1 == arr[idx]:
                # 가능
                if idx-L < 0:
                    return False
                else:
                    for j in range(idx-1, idx-L-1, -1):
                        if arr[j] != arr[idx-1] or visited[j] == 1:
                            return False
                    for j in range(idx-1, idx-L-1, -1):
                        visited[j] = 1
            else:
                return False
        if idx >= N:
            break
        tmp = arr[idx]
        idx += 1
        #print(idx, arr, visited)
        
        
    #print(arr, visited, 'arr2')
    return True

N, L = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

# 낙차가 1이상이면 못지나감
# 높이가 +- 1차이가 나기 시작하는지점에서 L+1지점이 막혀있지 않은경우 가능
# 겹치면 안됨 

answer = 0
# 행검사 열검사 다해야함
for i in range(N): # 행검사
    if solution(lst[i]) == True:
        answer += 1

for i in range(N):
    tmp = []
    for j in range(N):
        tmp.append(lst[j][i])
    if solution(tmp) == True:
        answer += 1
print(answer)