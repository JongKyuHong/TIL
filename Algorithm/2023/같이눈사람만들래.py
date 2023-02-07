import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
res = float('inf')

for start in range(N-3):
    for end in range(start+3, N):
        tmp = lst[start] + lst[end]
        start2, end2 = start+1, end-1
        while start2 < end2:
            tmp2 = lst[start2] + lst[end2]
            if res > abs(tmp-tmp2):
                res = abs(tmp-tmp2)
            if tmp > tmp2:
                start2 += 1
            elif tmp < tmp2:
                end2 -= 1
            else:
                print(0)
                exit()
print(res)

