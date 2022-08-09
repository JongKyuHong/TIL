for _ in range(3):
    a, b = input().split()
    ah,am,ase = a.split(":")
    bh,bm,bse = b.split(":")
    ah,am,ase = int(ah), int(am),int(ase)
    bh,bm,bse = int(bh), int(bm),int(bse)
    cnt = 0
    while 1:
        if ase == 60:
            ase = 0
            am += 1
            if am == 60:
                am = 0
                ah +=1
                if ah == 24:
                    ah,am,ase = 0,0,0
        if ah == bh and am == bm and ase == bse:
            break
        if int(str(ah)+str(am)+str(ase)) % 3 == 0:
            cnt += 1
        ase += 1
    print(cnt)