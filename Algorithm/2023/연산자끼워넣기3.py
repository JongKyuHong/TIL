# import sys
# input = sys.stdin.readline

# def calculate(nstack, ostack, idx, add, sub, mul, div):
#     global max_v, min_v
#     print(idx, add, sub, mul, div, nstack, ostack,'aa')
#     if idx == N+1:
#         while len(ostack) > 0:
#             #print(ostack, nstack,'o')
#             o = ostack.pop(0)
#             a, b = nstack.pop(0), nstack.pop(0)
#             if o == '+':
#                 nstack.insert(0, a + b)
#             else:
#                 nstack.insert(0, a - b)
#         max_v = max(max_v, nstack[-1])
#         min_v = min(min_v, nstack[-1])
#         return
    
#     if add > 0:
#         calculate(nstack+[nums[idx]], ostack+['+'], idx+1, add-1, sub, mul, div)
#     if sub > 0:
#         calculate(nstack+[nums[idx]], ostack+['-'], idx+1, add, sub-1, mul, div)
#     if mul > 0 and nstack:
#         nstack[-1] = nstack[-1]*nums[idx]
#         calculate(nstack, ostack, idx+1, add, sub, mul-1, div)
#     if div > 0 and nstack:
#         nstack[-1] = nstack[-1] // nums[idx]
#         calculate(nstack, ostack, idx+1, add, sub, mul, div-1)


# max_v = -1000000001
# min_v = 1000000001
# N = int(input())
# nums = list(map(int, input().split()))
# op = list(map(int, input().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈

# nstack = []
# ostack = []
# # 곱셈과 나눗셈인 경우는 계산 결과를 바로바로 스택에 저장?
# calculate(nstack, ostack, 0, op[0], op[1], op[2], op[3])
# print(max_v)
# print(min_v)

import sys
input = sys.stdin.readline

def calculate(num, idx, add, sub, mul, div):
    global max_v, min_v
    #print(idx, add, sub, mul, div, nstack, ostack,'aa')
    if idx == N:
        tmp = eval(num)
        max_v = max(max_v, tmp)
        min_v = min(min_v, tmp)
        return
    
    if add > 0:
        calculate(num + '+' + str(nums[idx]) , idx+1, add-1, sub, mul, div)
    if sub > 0:
        calculate(num + '-' + str(nums[idx]) , idx+1, add, sub-1, mul, div)
    if mul > 0:
        calculate(num + '*' + str(nums[idx]) , idx+1, add, sub, mul-1, div)
    if div > 0:
        calculate(num + '//' + str(nums[idx]) , idx+1, add, sub, mul, div-1)


max_v = -1000000001
min_v = 1000000001
N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈

nstack = [nums[0]]
ostack = []
# 곱셈과 나눗셈인 경우는 계산 결과를 바로바로 스택에 저장?
calculate(str(nums[0]), 1, op[0], op[1], op[2], op[3])
print(max_v)
print(min_v)