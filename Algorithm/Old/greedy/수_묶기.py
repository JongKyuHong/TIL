import heapq

T = int(input())
pn = []
nn = []
en = []
for _ in range(T):
    number=int(input())
    if number>1:
        pn.append(number)
    elif number<0:
        nn.append(number)
    else:
        en.append(number)
pn.sort(reverse=True)
nn.sort()
result = 0
if len(pn)%2 == 0:
    for i in range(0,len(pn)-1,2):
        result += pn[i]*pn[i+1]
else:
    for i in range(0,len(pn)-1,2):
        result += pn[i]*pn[i+1]
    result += pn[-1]

if len(nn)%2 == 0:
    for i in range(0,len(nn)-1,2):
        result += nn[i]*nn[i+1]
else:
    for i in range(0,len(nn)-1,2):
        result += nn[i]*nn[i+1]
    if 0 not in en:
        result += nn[-1]
result += sum(en)
print(result)




