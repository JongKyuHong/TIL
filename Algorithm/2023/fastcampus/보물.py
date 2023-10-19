import sys 
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A를 재배열하여 가장 작게 만들자
# 모든 경우 다해보자
# A의 가장 작은 수 X B의 가장 큰수

# 0 1 1 1 6
# 8 7 3 2 1
A.sort()
B.sort(reverse=True)
answer = 0
for i in range(N):
    answer += A[i]*B[i]
print(answer)

