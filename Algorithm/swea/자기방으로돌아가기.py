t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    hallway = [0 for i in range(201)]
    for x in range(n):
        start, end = map(int,input().split())
        if start > end:
            start, end = end, start
        for i in range((start+1)//2,(end+1)//2+1):
            hallway[i] += 1
    print(f'#{test_case} {max(hallway)}')