import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
res = float('inf')

for start in range(n-3):
    for end in range(start+3, n):
        tmp = lst[start] + lst[end]
        left, right = start+1, end-1
        while left < right:
            tmp2 = lst[left] + lst[right]
            if res > abs(tmp-tmp2):
                res = abs(tmp-tmp2)
            if tmp > tmp2:
                left +=1
            elif tmp < tmp2:
                right -= 1
            else:
                print(0)
                exit()
print(res)