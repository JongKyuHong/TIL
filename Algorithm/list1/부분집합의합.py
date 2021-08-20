# t = int(input())

# def check(n):
#     for i in range(1,13):
#         res = 0
#         cnt = 0
#         for j in range(n1):
#             if i & (1<<j):
#                 res += arr[j]
#                 cnt += 1
#         if res == k and cnt == n:
#             return 1
#     return 0

# for test_case in range(1,t+1):
#     n,k = map(int,input().split())
#     a = list(range(1,13))
#     cnt = 0
#     for i in range(1 << 12):
#         subset = []
#         sum_v = 0
#         for j in range(12):
#             if i & (1<<j):
#                 subset.append(a[j])
#                 sum_v += a[j]
#         if len(subset) == n and sum_v == k:
#             cnt += 1
#     print(f'#{test_case} {cnt}')
for i in range(1<<12):  # 0부터 2의12승-1 까지 돈다 
    # 즉 본문 코드는 모든 부분집합의 수를 꺼내어 j의 부분집합과 일치하는 놈의 정보를 꺼내옴?? 정도 밖에 이해가안되넹 ㅎ
    print(i,end =' ')
for j in range(12):
    print(j, end=' ')


