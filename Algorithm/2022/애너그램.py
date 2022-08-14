for _ in range(int(input())):
    a, b = input().split()
    adict = {}
    bdict = {}
    for i in a:
        if i in adict:
            adict[i] += 1
        else:
            adict[i] = 1
    for i in b:
        if i in bdict:
            bdict[i] += 1
        else:
            bdict[i] = 1
    if adict == bdict:
        print(a,'%',b,'are anagrams.')
    else:
        print(a,'%',b,'are NOT anagrams.')
