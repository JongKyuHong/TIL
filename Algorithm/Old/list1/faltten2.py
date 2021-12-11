for test_case in range(1,11):
    dump = int(input())
    boxes = list(map(int,input().split()))
    boxes.sort()
    for i in range(dump):
        boxes[0] += 1
        boxes[-1] -= 1
        boxes.sort()
    res = boxes[-1] - boxes[0]
    print(f'#{test_case} {res}')





