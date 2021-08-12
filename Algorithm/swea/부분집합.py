
#예시코드
# arr = [3,6,7,1,5,4]

# n = len(arr)

# import itertools as it

# t = int(input())

# for test_case in range(1,t+1):
#     n,k = map(int,input().split())
#     array = [i for i in range(1,13)]
#     result = it.combinations(array,n)
#     cnt = 0
#     for i in result:
#         if sum(i) == k:
#             cnt += 1
#     print(f'#{test_case} {cnt}')
import sys
sys.stdin = open('input.txt')

t = int(input())


def check(array,n,k): 
    length = len(array)
    for i in range(1,1<<length):
        cnt = 0
        a = []
        for j in range(length):
            if i & (1<<j):
                a.append(array[j])
                cnt += array[j]
        if cnt == k and len(a)==n:
            return 1
    return 0

for test_case in range(1,t+1):
    n,k = map(int,input().split())
    array = list(range(1,13))
    print(f'#{test_case}', check(array,n,k))


