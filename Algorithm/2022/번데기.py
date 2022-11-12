A = int(input())
T = int(input())
target = int(input())

idx = 0
people = 0
lst = [0,1,0,1,0,0,1,1]
while 1:
    for i in lst:
        if target == 0 and i == 0:
            T -= 1
        elif target == 1 and i == 1:
            T -= 1
        if T == 0:
            print(people)
            exit()
        people += 1
        people %= A
    lst.insert(4, 0)
    lst.append(1)