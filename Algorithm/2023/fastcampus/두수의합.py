import sys  
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
x = int(input())
answer = 0

for i in range(n-1):
    for j in range(i+1, n):
        if lst[i] + lst[j] == x:
            answer += 1
        elif lst[i] + lst[j] > x:
            break
print(answer)
