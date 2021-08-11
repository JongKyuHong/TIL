
#예시코드
# arr = [3,6,7,1,5,4]

# n = len(arr)

# for i in range(1<<n):
#     for j in range(n+1):
#         if i & (1<<j):
#             print(arr[j],end=', ')
#     print()
# print()
t = int(input())


def check(arr): 
    n = len(arr)
    for i in range(1,1<<n):
        cnt = 0
        for j in range(n):
            if i & (1<<j):
                cnt += arr[j]
        if cnt == 0:
            return True
    return False

for test_case in range(1,t+1):
    arr = list(map(int,input().split()))
    print(check(arr))


