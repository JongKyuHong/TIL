n,k = map(int,input().split()) # 원생의수, 조의개수
array = list(map(int,input().split()))

diff =[]
for i in range(n-1):
    diff.append(array[i+1]-array[i])
diff.sort()

answer = 0
for i in range(n-k):
    answer += diff[i]
print(answer)





