t = int(input())

for test_case in range(1,t+1):
    numbers = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    tc, num = input().split()
    text = list(input().split())
    result = [0]*10
    for i in range(int(num)):
        result[numbers.index(text[i])] += 1
    print(tc)
    for i in range(10):
        for j in range(result[i]):
            print(numbers[i],end=' ')






