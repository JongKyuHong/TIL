import sys

n = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))
count_num = [0]*10000001
result = [-1]*n
for i in range(len(array)): # n
   count_num[array[i]] += 1
stack = [0]
for i in range(1,n): # n
    while stack and count_num[array[stack[-1]]] < count_num[array[i]]:
        result[stack.pop()] = array[i]
    stack.append(i)
print(*result)




# import sys

# num = int(input())
# a = list(map(int, input().split(" ")))
# result = ["-1" for _ in range(num)]
# stack = [0]
# count = dict()
# for i in a:
#     try:
#         count[i] += 1
#     except:
#         count[i] = 1

# for i in range(num):
#     while stack and count[a[stack[-1]]] < count[a[i]]:
#         result[stack[-1]] = str(a[i])
#         stack.pop()
#     stack.append(i)
#     i+=1

# print(" ".join(result))