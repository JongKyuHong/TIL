n = int(input())
en = [500,100,50,10,5,1]
n = 1000 -n
count = 0
while n>0:
    if n >= en[0]:
        n -= en[0]
        count += 1
    elif n >= en[1]:
        n -= en[1]
        count += 1
    elif n >= en[2]:
        n -= en[2]
        count += 1
    elif n >= en[3]:
        n -= en[3]
        count += 1
    elif n >= en[4]:
        n -= en[4]
        count += 1
    else:
        n -= en[5]
        count += 1
print(count)

    
