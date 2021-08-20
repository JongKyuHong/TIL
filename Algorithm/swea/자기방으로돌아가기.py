t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    array = [list(map(int,input().split())) for _ in range(n)]
    hallway = [0 for i in range(400)]
    for x in array:
        if x[0] > x[1]:
            x[0],x[1] = x[1],x[0]        
        for  i in range(x[0],x[1]+1):
            hallway[i] += 1
    print(f'#{test_case} {max(hallway)}')









