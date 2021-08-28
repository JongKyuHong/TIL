n = int(input())
numbers = list(map(int, input().split()))
res = []
for i in range(n):
    res.insert(i-numbers[i],i+1)
print(res)










