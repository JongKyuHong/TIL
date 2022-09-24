for _ in range(int(input())):
    n = int(input())
    half = n//2
    
    room = [1]*(n+1)
    room[0] = 0
    for i in range(2,half+1): 
        j = 2
        k = i
        while k<=n:
            if room[k] == 1:
                room[k] = 0
            else:
                room[k] = 1
            k = i
            k *= j
            j += 1
    for i in range(half+1,n+1):
        if room[i] == 1:
            room[i] = 0
        else:
            room[i] = 1
    
    print(sum(room))