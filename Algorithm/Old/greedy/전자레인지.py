t = int(input())

secs = [300,60,10]
if t % secs[2] != 0:
    print(-1)
    exit(0)

for i in secs:
    print(t // i, end=' ')
    t %= i