n, m  = map(int, input().split())
pokemon = [input() for _ in range(n)]
res = [input() for _ in range(m)]

for i in res:
    if i.isalpha():
        print(pokemon.index(i)+1)
    else:
        print(pokemon[int(i)-1])
    
