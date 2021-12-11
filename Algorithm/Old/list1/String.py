for _ in range(10):
    tc = int(input())
    target = input()
    text = input()
    cnt = 0
    for i in range(len(text)-len(target)+1):
        if text[i] == target[0]:
            flag = 1
            for j in range(len(target)):
                if text[i+j] != target[j]:
                    flag = 0
            if flag == 1:
                cnt += 1
    print(f'#{tc} {cnt}')





