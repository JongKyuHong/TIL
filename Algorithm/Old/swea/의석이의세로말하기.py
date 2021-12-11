tc = int(input())

for test_case in range(1,tc+1):
    text = [input() for _ in range(5)]
    result = [[] for _ in range(15)]
    for i in text:
        for j in range(len(i)):
            result[j].append(i[j])
    print(f'#{test_case}',end=' ')
    for i in result:
        for j in i:
            print(j,end='')
    print()


    #print(f'#{test_case}', ''.join(map(str,zip(*text))))
