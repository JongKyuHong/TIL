t = int(input())

def binary_search(target):
    start = 1
    end = p
    cnt = 0
    while start<end:
        cnt += 1
        mid = int((start+end)/2)
        if mid > target:
            end = mid
        elif mid < target:
            start = mid
        else:
            break
    return cnt

for test_case in range(1,t+1):
    p,a,b = map(int,input().split())
    cnt1 = binary_search(a)
    cnt2 = binary_search(b)
    print(f'#{test_case}',end=' ')
    if cnt1 > cnt2:
        print('B')
    elif cnt1 < cnt2:
        print('A')
    else:
        print('0')


    