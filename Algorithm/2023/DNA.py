import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dna = []
for _ in range(N):
    dna.append(input().rstrip())

ans = ''
cnt = 0
for i in range(M):
    alpha = [0, 0, 0, 0]
    for j in range(N):
        if dna[j][i] == 'A':
            alpha[0] += 1
        elif dna[j][i] == 'C':
            alpha[1] += 1
        elif dna[j][i] == 'G':
            alpha[2] += 1
        elif dna[j][i] == 'T':
            alpha[3] += 1
    idx = alpha.index(max(alpha))
    if idx == 0:
        ans += 'A'
        cnt += alpha[1] + alpha[2] + alpha[3]
    elif idx == 1:
        ans += 'C'
        cnt += alpha[0] + alpha[2] + alpha[3]
    elif idx == 2:
        ans += 'G'
        cnt += alpha[0] + alpha[1] + alpha[3]
    else:
        ans += 'T'
        cnt += alpha[0] + alpha[1] + alpha[2]
print(ans)
print(cnt)