for _ in range(int(input())):
    n = int(input())
    maxcol,maxname = 0, ''
    for _ in range(n):
        name, value = input().split()
        if maxcol < int(value):
            maxcol = int(value)
            maxname = name
    print(maxname)            
    