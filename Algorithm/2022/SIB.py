n = int(input())
temp = list(map(int, input().split()))
num = []
num.append(temp[0])
for i in range(1, n):
    num.append(num[i-1]+temp[i])

answer = 0
for i in range(n):
    answer += temp[i]*(num[n-1]-num[i])
print(answer)