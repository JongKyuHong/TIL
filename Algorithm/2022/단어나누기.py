import sys
input = sys.stdin.readline

word = list(input().rstrip())
res = []
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]

        a.reverse()
        b.reverse()
        c.reverse()
        res.append("".join(a+b+c))
res.sort()
print(res[0])