a = 24500
d = 750
phase = 32
ans = 0
while phase < 51:
    phase += 1
    a += 750
    ans += a
print(ans-(48000*5)-(12000*36))

# 8000 + 4000 = 12000