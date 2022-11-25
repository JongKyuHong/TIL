import sys
input = sys.stdin.readline
idx = 1
while 1:
    n = int(input())
    if n == 0:
        break
    names = [input().rstrip() for _ in range(n)]
    arr = []
    clear = []
    for _ in range(2*n-1):
        num, check = input().rstrip().split()
        if num not in arr:
            arr.append(num)
        else:
            arr.remove(num)
    
    print(idx, names[int(arr[0])-1])
    idx += 1