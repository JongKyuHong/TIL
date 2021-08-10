t = int(input())

for test_case in range(1,t+1):
    n,m = map(int,input().split())
    arr = []
    for _ in range(n):
        arr.append(list(input()))
    for j in range(n):
        for k in range(n-m+1):
            ga_arr = arr[j][k:k+m]
            se_arr = [arr[x][j] for x in range(k,(k+m))]
            if ga_arr == ga_arr[::-1]:
                hwe=ga_arr
            elif se_arr == se_arr[::-1]:
                hwe=se_arr
    print('#'+str(test_case+1),end=' ')
    for j in hwe:
        print(j,end='')
    print()

    
                        
    
        




