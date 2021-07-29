t = int(input())

for _ in range(t):
    start,end = map(int,input().split())
    d = [0,1,2]
    s = start + 1
    e = end - 1
    count = 0
    d_sum = 0
    while d_sum<((e-s)/2):
        if d_sum + d[-1] < ((e-s)/2): # 1 <= 2, 3<=2
            d_sum += d[-1] # 1
            count += 1 # 1
            d.append(d[-1]+1) # 2
        elif d_sum+d[-1] == ((e-s)/2):
            d_sum += d[-1]
            count += 1
            break
        else:
            for i in range(len(d)-1,len(d)-4,-1):
                if d_sum + d[-i] < ((e-s)/2): # 1+1 <= 2
                    d_sum += d[-i]
                    count += 1
                    if d[-i]+1 not in d:
                        d.append(d[-1]+1)
                elif d_sum + d[-i] == ((e-s)/2):
                    d_sum += d[-i]
                    count += 1 
                    break
    if e-s%2:
        print(2*count+3)
    else:
        print(2*count+2)

