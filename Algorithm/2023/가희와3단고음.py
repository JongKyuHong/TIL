import sys
N, A, D = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

cnt = 0
x = 0
for i in range(N):
    if arr[i] == A + (x*D): #등차가 D인 수열로 숫자 올려주기
        cnt += 1
        x += 1
print(cnt)