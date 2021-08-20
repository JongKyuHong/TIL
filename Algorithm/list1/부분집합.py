# bit = [0, 0, 0, 0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)

# arr = [3,6,7,1,5,4]
# n = len(arr)
# for i in range(1<<n):
# 	for j in range(n+1):
#         if i & (1<<j):
#             print(arr[j],end=' ')
#     print()
# print()

# 10개의 정수를 입력받아 부분집합의 합이 0이 되는 것이 존재하는지 계산하는 함수를 짜보자

# import sys
# sys.stdin = open('input.txt')

# t = int(input())


# def check(arr):
#     n = len(arr)
#     for i in range(1,1<<n):
#         cnt = 0
#         for j in range(n):
#             if i & (1<<j):
#                 cnt += arr[j]
#         if cnt == 0:
#             return True
#     return False

# for test_case in range(1,t+1):
#     arr = list(map(int,input().split()))
#     print(check(arr))