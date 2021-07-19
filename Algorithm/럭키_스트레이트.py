n = int(input())
n = str(n)

length = len(str(n))
n1 = n[:int(length/2)]
n2 = n[int(length/2):]
sum1 = 0
sum2 = 0
for i in n1:
    sum1 += int(i)
for i in n2:
    sum2 += int(i)
print('LUCKY') if sum1 == sum2 else print('READY')