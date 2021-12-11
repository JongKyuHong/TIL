t = int(input())

for test_case in range(1,t+1):
    dump = int(input())
    array = list(map(int,input().split()))
    
    for _ in range(dump):
        array[array.index(min(array))] += 1
        array[array.index(max(array))] -= 1
    result = max(array) - min(array)
    print(f'#{test_case} {result}')
