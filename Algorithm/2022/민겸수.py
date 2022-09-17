string = list(input())

min_v, max_v = '',''
cnt = 0
for i in range(len(string)):
    if string[i] == 'M':
        cnt += 1
    else:
        if cnt > 0:
            max_v += str(5 * (10**cnt))
            min_v += str(10**(cnt-1))
            min_v += '5'
        else:
            min_v += '5'
            max_v += '5'
        cnt = 0

if cnt > 0:
    max_v += '1'*cnt
    min_v += str(10**(cnt-1))

print(int(max_v))
print(int(min_v))