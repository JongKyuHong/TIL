import sys 
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0
while sum(arr) != 0:
    check = 0
    for i in range(N):
        if arr[i] % 2 != 0 or arr[i] == 0 or arr[i] == 1:
            if arr[i] == 0:
                continue
            else:
                arr[i] -= 1
                cnt += 1
            check = 1
    if check == 0:
        for i in range(N):
            arr[i] //= 2
        cnt += 1
print(cnt)