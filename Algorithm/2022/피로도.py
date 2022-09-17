a, b, c, m = map(int, input().split())
# a는 피로도 b는 처리한 일의 양, c는 한시간 쉬었을때 줄어드는 피로도, m은 피로도의 최대치
res = 0 # 마지막에 반환할 일의 총량
piro = 0
hour = 0
while hour < 24:
    hour += 1
    if (piro+a) > m:
        if piro - c < 0:
            piro = 0
        else:
            piro -= c
    else:
        res += b
        piro += a
print(res)