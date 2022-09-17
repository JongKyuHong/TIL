h1,m1,s1 = map(int, input().split(":"))
h2,m2,s2 = map(int, input().split(":"))

if h1 == h2 and m1 == m2 and s1 == s2:
    print("24:00:00")
    exit()
h, m = 0, 0

s = s2 - s1
if s < 0:
    m -= 1
    s += 60

m += m2 - m1
if m < 0:
    h -= 1
    m += 60

h += h2 - h1
if h < 0:
    h += 24

h = str(h).zfill(2)
m = str(m).zfill(2)
s = str(s).zfill(2)

print(f'{h}:{m}:{s}')