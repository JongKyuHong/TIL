import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input())
alpha = [[0 for _ in range(26)] for _ in range(len(S))]
alpha[0][ord(S[0])-97] = 1
for i in range(1, len(S)):
    alpha[i][ord(S[i])-97] = 1
    for j in range(26):
        alpha[i][j] += alpha[i-1][j]
for _ in range(q):
    a, b, c = input().rstrip().split()
    b, c = int(b), int(c)
    if b == 0:
        print(alpha[c][ord(a)-97])
    else:
        print(alpha[c][ord(a)-97] - alpha[b-1][ord(a)-97])