def check(a):
    l = len(a)
    for i in range(l//2):
        if a[i] != a[l-i-1]:
            return False
    return True

for _ in range(10):
    tc = int(input())
    length = 100
    map_list = [input() for _ in range(100)]
    map_list2 = []
    for i in range(n):
        str_temp = ''
        for k in range(n):
            str_temp += map_list[k][i]
        map_list2.append(str_temp)
    n = 100
    res = 0
    for i in range(length, 0, -1):
        if res >= i:
            break
        for j in range(n):
            if res == i:
                break
            for k in range(n-i+1):
                if check(map_list[j][k:k+i]) or check(map_list2[j][k:k+i]):
                    res = i
                    break
    print(f'#{tc} {res}')


