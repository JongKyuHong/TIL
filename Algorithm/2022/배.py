import sys
input = sys.stdin.readline

n = int(input())
limit = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
boxes = sorted((map(int, input().split())), reverse=True)
if max(limit) < max(boxes):
    print(-1)
else:
    time = 0
    while boxes:
        for i in range(n):
            for j in range(len(boxes)):
                if limit[i] >= boxes[j]:
                    boxes.pop(j)
                    break
        time += 1
    print(time)