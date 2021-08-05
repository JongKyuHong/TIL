n = int(input())
tryangle = []
for _ in range(n):
    tryangle.append(int(input()))
tryangle.sort(reverse=True)
maxa = 0
for i in range(0,len(tryangle)-2):
    if tryangle[i] < tryangle[i+2]+tryangle[i+1]:
        maxa = max(maxa,tryangle[i]+tryangle[i+1]+tryangle[i+2])
    else:
        continue
if maxa == 0:
    print(-1)
else:
    print(maxa)
