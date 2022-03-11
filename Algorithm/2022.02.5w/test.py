nlist = list(map(int, input().split()))
lista = [1,1,2,2,2,8]
for i in range(len(nlist)):
    if len(nlist) != i-1:
        print(lista[i]-nlist[i], end=' ')
    else:
        print(lista[i]-nlist[i])
    
    