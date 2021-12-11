n, k = map(int, input().split())  # n학생 참가수, k 한방에 배정할수있는 최대 인원수
student = [list(map(int, input().split())) for _ in range(n)]
girls = [0] * 6
boys = [0] * 6
for a,b in student:
    if a == 0:
        girls[b-1] += 1
    else:
        boys[b-1] += 1
cnt = 0
for i in girls:
    if i == 0:
        continue
    elif i // k < 1:
        cnt += 1
    else:
        if i % k == 0:
            cnt += (i//k)
        else:
            cnt += (i//k) + 1
for i in boys:
    if i == 0:
        continue
    elif i // k < 1:
        cnt += 1
    else:
        if i % k == 0:
            cnt += (i//k)
        else:
            cnt += (i//k) + 1
print(cnt)


