for _ in range(10):
    tc = int(input())
    matrix = [input() for _ in range(100)]
    matrix2 = list(zip(*matrix))
    cnt = 1
    for k in range(100):
        if cnt >= k:
            break
        for i in range(100,0,-1):
            if cnt >= i:
                break
            for j in range(100-i+1):
                a = matrix[k][j:j+i]
                b = matrix[k][j:j+i]
                if a == a[::-1] or b == b[::-1]:
                    cnt = i
                    break
    print(f'#{tc} {cnt}')

