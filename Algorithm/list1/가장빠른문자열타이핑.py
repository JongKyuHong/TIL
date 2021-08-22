t = int(input())

for test_case in range(1,t+1):
    text_a, b = input().split()
    res = 0
    len_a = len(text_a)
    len_b = len(b)
    i = 0
    while i < len_a:
        if text_a[i] == b[0]:
            if text_a[i:i+len_b] == b:
                res += 1
                i += len_b
            else:
                i += 1
        else:
            i += 1
    result = len(text_a) - res*len(b) + res
    print(f'#{test_case} {result}')







