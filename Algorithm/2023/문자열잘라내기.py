from collections import defaultdict
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
table = [list(input().rstrip()) for _ in range(R)]
cnt = 0
result = 0
start, end = 0, R-1
while start <= end:
    mid = (start+end)//2
    flag = 0
    dict = defaultdict(int)
    for j in range(C):
        tmp = ''
        for i in range(mid, R):
            tmp += table[i][j]
        if not dict[tmp]:
            dict[tmp] += 1
        else:
            flag = 1
            break
    if not flag:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
                

        


