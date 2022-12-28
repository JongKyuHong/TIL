import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n의 약수중 k번째로 작은 수
cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
        if cnt == k:
            print(i)
            exit()
print(0)