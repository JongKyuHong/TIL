import sys 
input = sys.stdin.readline

time = 10**8
for _ in range(int(input())):
    S, N, T, L = input().rstrip().split()
    N, T = int(N), int(T)
    S = S[2:-1]
    L = time*(int(L))
    if S == 'N':
        if N*T <= L:
            print('May Pass.')
        else:
            print('TLE!')
    elif S == 'N^2':
        if (N**2)*T <= L:
            print('May Pass.')
        else:
            print('TLE!')
    elif S == 'N!':
        flag = 1
        target = T
        for i in range(2, N+1):
            target *= i
            if target > L:
                print('TLE!')
                flag = 0
                break
        if flag:
            print('May Pass.')
    elif S == 'N^3':
        if (N**3)*T <= L:
            print('May Pass.')
        else:
            print('TLE!')
    elif S == '2^N':
        if (2**N)*T <= L:
            print('May Pass.')
        else:
            print('TLE!')
