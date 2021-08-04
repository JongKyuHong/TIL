n = int(input())
n1 = []
n2 = []
n3 = []
for _ in range(n):
    number = int(input())
    if number > 1:
        n1.append(number)
    elif number < 0:
        n2.append(number)
    else:
        n3.append(number)
n1.sort(reverse=True)
n2.sort()
result = 0
if len(n1)%2 == 0:
    for i in range(0,len(n1)-1,2):
        result += n1[i]*n1[i+1]
else:
    for i in range(0,len(n1)-1,2):
        result += n1[i]*n1[i+1]
    result += n1[-1] 
if len(n2)%2 == 0:
    for i in range(0,len(n2)-1,2):
        result += n2[i]*n2[i+1]
else:
    for i in range(0,len(n2)-1,2):
        result += n2[i]*n2[i+1]
    if 0 not in n3:
        result += n2[-1]  
result += sum(n3)
print(result)



