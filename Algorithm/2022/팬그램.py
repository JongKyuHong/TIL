import sys
input = sys.stdin.readline


for i in range(1, int(input())+1):
    arr = {}
    words = input().rstrip()
    for word in words:
        if word.isalpha():
            if word.lower() not in arr:
                arr[word.lower()] = 1
            else:
                arr[word.lower()] += 1
    
    idx = 0
    flag = 0
    if len(arr.keys()) == 26:
        min_v = float('inf')
        for k, v in arr.items():
            min_v = min(min_v, v)
        if flag:
            print(f'Case {i}: Not a pangram')
        else:
            if min_v == 1:
                print(f'Case {i}: Pangram!')
            elif min_v == 2:
                print(f'Case {i}: Double pangram!!')
            else:
                print(f'Case {i}: Triple pangram!!!')   
    else:
        print(f'Case {i}: Not a pangram')
            