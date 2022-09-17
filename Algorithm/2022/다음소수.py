import math
for _ in range(int(input())):
    n = int(input())
    
    while 1:
        if n == 0 and n == 1:
            n+=1
            continue
        flag = 1
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                flag = 0
                break
        if flag:
            print(n)
            break
        n += 1