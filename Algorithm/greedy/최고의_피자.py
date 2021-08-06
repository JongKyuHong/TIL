n = int(input()) # 토핑의 종류
a,b = map(int,input().split()) # 도우의 가격 a 토핑의 가격 b
c = int(input()) # 도우의 칼로리
d = []
for _ in range(n): # 각 토핑의 열량
    d.append(int(input()))
d.sort(reverse=True)
cnt = 0
maxa = 0
print(c)
for i in range(n):
    cnt += 1
    if maxa < (c+d[i])/(a+(b*cnt)):
        maxa = (c+d[i])/(a+(b*cnt))
        c += d[i]
print(int(maxa))