n = int(input())
list_n = list(str(n))
num = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}

for i in list_n:
    if i == '9':
        num['6'] += 1
    else:
        num[i] += 1
        
res = 0
for k,v in num.items():
    if k == '6':
        res = max(res, (v+1)//2)
    else:
        res = max(res, v)
        
print(res)