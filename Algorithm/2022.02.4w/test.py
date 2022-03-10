n = int(input())

for _ in range(n):
    print('* '* (n - n//2))
    print(n)
    print(' *'* (n//2))