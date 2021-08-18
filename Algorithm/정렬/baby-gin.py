# 3장이 연속 run
# 3장이 동일한 번호 triplet
t = int(input())
for _ in range(t):
    num = list(map(int,input()))
    num.sort()
    run = 0
    triplet = 0
    for i in range(1,len(num)):
        if num[i] == num[i-1]+1:
            run += 1
        elif num[i] == num[i-1]:
            for j in range(i,len(num)):
                if num[i] == num[i-1]:
                    triplet +=1
                    if triplet == 3:
                        triplet = 0
                        break
                else:
                    triplet = 0
                    break
    if run + triplet == 6:
        print('baby-gin')
    else:
        print('nono')




