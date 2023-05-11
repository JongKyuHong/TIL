start = 15500
sum_v = start
cnt = 0
while start < 38000:
    start += 750
    sum_v += start
    cnt += 1
print(sum_v+(36000*5))
print(cnt)