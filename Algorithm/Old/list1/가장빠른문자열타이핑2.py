t = int(input())

for test_case in range(1,t+1):
    a, b = input().split()
    len_a, len_b = len(a),len(b)
    res = 0
    i = 0
    while i <len_a:
        if a[i] == b[0]:
            if a[i:i+len_b] == b:
                res += 1
                i += len_b
            else:
                i += 1
        else:
            i += 1
    result = len_a - res*len_b + res
    print(f'#{test_case} {result}')








