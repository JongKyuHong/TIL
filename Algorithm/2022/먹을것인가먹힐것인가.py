def binary_search(lst, a):
    answer = -1
    start, end = 0, len(lst)-1 
    while start <= end:
        mid = (start+end)//2
        if lst[mid] < a:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer
        


for _ in range(int(input())):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    cnt = 0
    for a in A:
        cnt += (binary_search(B, a)+1)
    print(cnt)