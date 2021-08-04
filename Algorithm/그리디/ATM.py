n = int(input())

p1 = list(map(int,input().split()))
p1.sort()
sum = 0
for i in range(len(p1)):
    if i == 0:
        sum = p1[0]
    else:
        for j in p1[:i+1]:
            sum += j
print(sum)
