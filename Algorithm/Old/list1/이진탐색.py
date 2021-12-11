t = int(input())

def binary_search(target):
    start = 1
    end = p
    cnt = 0
    while start <= end:
        mid = (start+end)//2
        cnt += 1
        if mid == target:
            return cnt
        elif mid > target:
            end = mid
        else:
            start = mid
for test_case in range(1,t+1):
    p, a, b = map(int,input().split())
    a1 = binary_search(a)
    b1 = binary_search(b)
    if a1 > b1:
        print(f'#{test_case} B')
    elif a1 < b1:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')

