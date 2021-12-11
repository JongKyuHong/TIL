import heapq

n , k =map(int,input().split())
real_k = k
array = input()
stack = [array[0]]
i = 1
check = 1 # 뭐를 체크하기위해? 1을 잡기위해
while check < n-k and k>0 and stack and i<len(array): # k가 0보다 큰경우 왜? k를 팝할때마다 줄여서k가 0이되면 와일문을 나오고 아래서 한번에 넣게
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
    for h in range(n-real_k):
        print(stack[h],end='')
elif k == 0:
    for j in range(i,n):
        stack.append(array[j])
    print(''.join(stack))
else:
    print(''.join(stack))
        
    
