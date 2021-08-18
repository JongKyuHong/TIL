for test_case in range(1,11):
    dump = int(input()) #  덤프 횟수
    height = sorted(list(map(int,input().split())))
    
    for _ in range(dump):
        height[-1] -= 1
        height[0] += 1
        height.sort()
    result = max(height) - min(height)
    print(f'#{test_case} {result}')









