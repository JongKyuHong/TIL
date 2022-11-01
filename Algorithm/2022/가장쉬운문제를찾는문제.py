N=int(input())

name=[0]*N
rank=[0]*N

for i in range(N):
    Str=input()
    name[i]=Str[:len(Str)-2]
    rank[i]=int(Str[-1])

Dict=dict(zip(rank,name))

print(Dict[min(Dict.keys())])