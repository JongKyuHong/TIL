import sys 
input = sys.stdin.readline

N = int(input())
K = int(input())

lst = list(map(int, input().split()))
lst.sort()
distance = []
for i in range(1, N):
    distance.append(lst[i] - lst[i-1])
distance.sort(reverse=True)

for i in range(K-1):
    distance[i] = 0
print(sum(distance))