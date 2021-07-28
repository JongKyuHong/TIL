import heapq

n , k =map(int,input().split())
real_k = k
array = input()
stack = [array[0]]
i = 1
check = 1 # 뭐를 체크하기위해? 1을 잡기위해
while check < n-k and k>0 and stack and i<len(array): # k가 0보다 큰경우 왜? k를 팝할때마다 줄여서k가 0이되면 와일문을 나오고 아래서 한번에 넣게
    print(stack)
    if stack[-1] >= array[i]:
        stack.append(array[i])
        i += 1
    else:
        stack.pop()
        k -= 1
    if not stack:
        stack.append(array[i])
        i += 1
if len(array) == i:
    print('hi')
    for h in range(n-real_k):
        print(stack[h],end='')
elif k == 0:
    for j in range(i,n):
        stack.append(array[j])
    print(''.join(stack))
else:
    print(''.join(stack))
# for i in range(1,n):
#     if flag == 1:
#         break
#     if count == k: # k만큼 이미 다 제거하였다면 나머지는 스택에 그냥 넣는다.
#         for j in range(i,n):
#             stack.append(array[j])
#         break
#     if stack[-1] >= array[i]: # 스택의 마지막 값이 array[i]보다 크면 array[i]의 값을 그냥 넣는다.
#         stack.append(array[i])
#     else: # 새로들어온 값이 더 크게되면 스택을 뺀다 언제까지? 스택값이 새로들어온값보다 클때까지
#         stack.pop()
#         count += 1
#         #if stack: # 만약 방금뺀것이 마지막값이 아니라면
#         while stack: # 마지막값까지 while을 돈다.
#             if count == k:
#                 for j in range(i,n):
#                     stack.append(array[j])
#                 flag = 1
#                 break
#             if stack[-1] <= array[i] and stack: #새로들어온값이 더 크고 스택이 남아있다면
#                 stack.pop()
#                 count += 1
#             elif stack[-1] > array[i]: # 새로들어온값이 더 작거나 스택이 없다면 
#                 stack.append(array[i])
#                 break
#             elif not stack:
#                 stack.append(array[i])
#                 break
#         if not stack: # 만약에 스택이 비어있다면
#             stack.append(array[i])
#         # else: # 스택이 그냥 비어있다면
#         #     stack.append(array[i])
# print(''.join(stack))
        
    
