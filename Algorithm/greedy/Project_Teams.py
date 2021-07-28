n = int(input())

array = list(map(int,input().split()))
array.sort()
sum1 = 10**6
while array:
    sum1 = min(sum1,array.pop(0) + array.pop(-1))
print(sum1)