
n = int(input())

milk = []
for _ in range(n):
    milk.append(int(input()))
milk.sort(reverse=True)
result = 0
index = 0
for i in range(0,len(milk)):
    if index == 2:
        index = 0
    else:
        result += milk[i]
        index += 1
    
print(result)