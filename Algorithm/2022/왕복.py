n, k = map(int, input().split())

value = list(map(int, input().split()))
len_value = len(value)
value = [0] + value + value[::-1]
new_len = len(value)
if k == 0:
    print(1)
    exit()
for i in range(new_len):
    if k - value[i] > 0:
        k -= value[i]
    elif k - value[i] == 0:
        s = i + 1
        if s > len_value:
            print(1+len_value - s%len_value)
        else:
            print(s)
        break
    else:
        if i > len_value:
            print(1+len_value - i%len_value)
        else:
            print(i)
        break



