import sys
input = sys.stdin.readline

n = int(input()) # 학기가 몇분인지 나타내는 정수
res = 0
job = []
for _ in range(n):
    data = input().rstrip().split()
    if data[0] == '1':
        score, s_time = int(data[1]), int(data[2])
        s_time -= 1
        if s_time > 0:
            job.append((score, s_time))
        else:
            res += score
    else:
        if job:
            s,t = job.pop()
            t -= 1
            if t > 0:
                job.append((s,t))
            else:
                res += s
print(res)