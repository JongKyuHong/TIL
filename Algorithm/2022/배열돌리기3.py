k=int(input())
cnt=0
n=0
answer=[]
result=''
while 1:
    n+=1
    cnt+=2**n
    if cnt>=k:
        break
idx=k-2**n+1
for i in range(n):
    answer.append(idx%2)
    idx//=2
answer.reverse()
for i in range(len(answer)):
    if answer[i]==1:
        result+='7'
    else:
        result+='4'
print(int(result))