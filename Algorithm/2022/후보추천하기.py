import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
arr = {}
recommends = list(map(int, input().split()))
for recommend in recommends:
    if recommend not in arr.keys():
        if len(arr.keys()) == n:
            min_v = float('inf')
            min_k = -1
            for k, v in arr.items():
                if v < min_v:
                    min_v = v
                    min_k = k
            arr.pop(min_k)
        arr[recommend] = 1
    else:
        arr[recommend] += 1

print(*sorted(arr.keys()))