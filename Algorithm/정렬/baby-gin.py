# 3장이 연속 run
# 3장이 동일한 번호 triplet
t = int(input())
for _ in range(t):
    num = list(map(int,input()))
    count_num = [0] * (len(num)+1)
    for i in range(len(num)):
        count_num[num[i]] += 1
    



