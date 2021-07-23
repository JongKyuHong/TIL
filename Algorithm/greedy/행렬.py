n,m = map(int,input().split())
a = []
b = []
for _ in range(n):
    a.append(input())

for _ in range(n):
    b.append(input())
answer = 0
def col_check(a,b): #행불러와서 열끼리 검사
    global answer
    for i in range(m):
        print(a[i])
        if a[i] != b[i]:
            answer += 1
            #for j in range(n):
                # if a[i][j] == '1':
                #     a[i][j] = '0'
                # else:
                #     a[i][j] = '1'
    return a,b
for i in range(n):
    col_check(a[i],b[i])
print(answer)

