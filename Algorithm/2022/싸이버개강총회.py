S, E, Q = input().split()

S = int(S[:2] + S[3:])
E = int(E[:2] + E[3:])
Q = int(Q[:2] + Q[3:])

names = {}
res = 0
while 1:
    data = input()
    if len(data) < 3:
        break 
    H, N = data.split()
    H = int(H[:2]+H[3:])
    if H <= S:
        names[N] = 1
    elif E <= H <= Q:
        if N in names:
            names[N] += 1

for k, v in names.items():
    if v >= 2:
        res += 1
print(res)

