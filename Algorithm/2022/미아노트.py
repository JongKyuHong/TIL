import sys
input = sys.stdin.readline

n, h, w = map(int, input().split())

words = []
for _ in range(h):
    words.append(list(input().rstrip()))

def find(r, c):
    for i in range(r, r+h):
        for j in range(c, c+w):
            if words[i][j] != '?':
                return words[i][j]
    return 0

res = ''

for j in range(0, n*w, w):
    target = find(0, j)
    if target:
        res += target
    else:
        res += '?'
print(res)