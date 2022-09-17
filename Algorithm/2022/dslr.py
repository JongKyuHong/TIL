from collections import deque
import sys
input = sys.stdin.readline
            

for T in range(int(input())):
    a, b = map(int,input().split())
    visited = [0] * 10001
    visited[a] = 1

    q = deque()
    q.append((a,''))
    while q:
        num, path = q.popleft()
        visited[num] = 1
        if num == b:
            print(path)
            break
        num2 = (2*num)%10000
        if not visited[num2]:
            q.append((num2,path+"D"))
            visited[num2] = True
        
        num2 = (num-1)%10000
        if not visited[num2]:
            q.append((num2, path+'S'))
            visited[num2] = 1
        
        num2 = (10*num+(num//1000))%10000
        if not visited[num2]:
            q.append((num2,path+"L"))
            visited[num2] = True
            
        num2 = (num//10+(num%10)*1000)%10000
        if not visited[num2]:
            q.append((num2,path+"R"))
            visited[num2] = True   