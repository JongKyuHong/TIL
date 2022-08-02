import math

n = int(input())
if n <= 2:
    print(2)
elif n <= 3:
    print(3)
elif n <= 5:
    print(5)
elif n <= 7:
    print(7)
else:
    while 1:
        flag = 1
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                flag = 0
                break
        if flag:
            str_n = str(n)
            if str_n == str_n[::-1]:
                print(n)
                break
            # len_ = len(str_n)
            # if len_ % 2:
            #     if str_n[:len_//2+1] == str_n[:len_//2-1:-1]:
            #         print(n)
            #         break
            # else:
            #     if str_n[:len_//2] == str_n[:len_//2-1:-1]:
            #         print(n)
            #         break
        n += 1
# n = '101231'
# print(n[:len(n)//2], n[:len(n)//2-1:-1])
