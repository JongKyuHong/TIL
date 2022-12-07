import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # n자리숫자, 지울수있는 숫자 k
num = list(input())
k, stack = K, []

for i in range(N):
    while k > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        k -= 1
    stack.append(num[i])
print(''.join(stack[:N-K]))