n,q = map(int,input().split()) # 통나무 개수 , 질문의 개수
log =[]
for _ in range(n):
    log.append(list(map(int,input().split())))
question = []
for _ in range(q):
    question.append(list(map(int,input().split())))
result = [0]*(n+1)
check = log[0][1]
for i in range(n-1):
    if check >= log[i+1][0]:
        if check < log[i+1][1]:
            check = log[i+1][1]
        result[i+1] = 1
    else:
        break
for i in question:
    if result[i[1]-1] == 1:
        print(1)
    else:
        print(0)