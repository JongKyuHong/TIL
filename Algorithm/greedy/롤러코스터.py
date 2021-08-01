r,c = map(int,input().split())

array = []
for _ in range(r):
    array.append(list(map(int,input().split())))

# r이 짝수일때 분기가 나뉜다.
# c가 홀수일때 세로로 볼수 있다. 즉 행의 갯수가 홀수일때 다 볼수있다 열도 마찬가지
result = ''

if r%2 and c%2: # 33이라고 생각해보자
    for i in range(r):
        if i%2:
            for _ in range(c-1):
                result += 'L'  
        else:
            for _ in range(c-1):
                result += 'R'
        result +='D'
    print(result[:len(result)-1])
elif r%2==0 and c%2: # 행은 짝인데 열은 홀일때 즉 세로로 봐야한다.
    for i in range(r):
        if i%2:
            for _ in range(c-1):
                result += 'D'  
        else:
            for _ in range(c-1):
                result += 'U'
        result +='R'
    print(result[:len(result)-1])
elif r%2 and c%2==0: # 행은 홀이고 열은 짝일때 
    for i in range(r):
        if i%2:
            for _ in range(c-1):
                result += 'L'  
        else:
            for _ in range(c-1):
                result += 'R'
        result +='D'
    print(result[:len(result)-1])
else: #행이 짝이고 열도 짝일때
    result1 = 0
    result2 = 0
    result3 = ''
    result4 = ''
    for i in range(r-1):
        for j in range(c):
            result1 += array[i][j]
            if i % 2 == 0:
                result3 += 'R'
            else:
                result3 += 'L'
        result3 = result3[:len(result3)-1]
        result3 += 'D'
    result1 += array[r-1][c-1]
    result3 = result3[:len(result3)-1]
    for i in range(r):
        if i == r-2:
            result2 += array[i][0]
            result4 += 'D'
            continue
        for j in range(c):
            result2 += array[i][j]
            if i%2 == 0 and i>r-2:
                result4 += 'L'
            elif i%2 == 0:
                result4 += 'R'
            elif i%2 and i>r-2:
                print('hi2')
                result4 += 'R'
            elif i%2:
                result4 += 'L'
        result4 = result4[:len(result4)-1]
        result4 += 'D'
    result4 = result4[:len(result4)-1]
    if result1 > result2:
        print(result1)
        print(result3)
    else:
        print(result2)
        print(result4)

