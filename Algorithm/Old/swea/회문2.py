#import sys
#sys.stdin = open('input.txt')

# def check(lst):
#     for i in range(len(lst)//2):
#         if lst[i] != lst[-i-1]:
#             return False
#     return True


# for _ in range(10):
#     tc = int(input())
#     array = [list(input()) for _ in range(5)]
#     for j in range(5):
#         array2 = [array[i][j] for i in range(5)]
#         for k in range(5-j-1):
#             check()

#     print(array2)
#     cnt = 1
#     for i in range(5, 1, -1):
#         if cnt >= i:
#             break
#         for j in range(5-i+1):
#             if cnt == i:
#                 break
#             for lst,lst2 in zip(array, array2):
#                 if check(lst[j:j+i]) or check(lst2[j:j+i]):
#                     cnt = i
#     print(f'#{tc} {cnt}')
