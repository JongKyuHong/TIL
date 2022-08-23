import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n은 dna갯수, m은 문자열 길이

dna = [input().rstrip() for _ in range(n)]

words = ['A','T','G','C']
res = ''
ans = 0
for i in range(m):
    char = ''
    min_v = sys.maxsize
    for word in words:
        cnt = 0
        for j in range(n):
            if word != dna[j][i]:
                cnt += 1
        if min_v > cnt:
            min_v = cnt
            char = word
        elif min_v == cnt:
            if ord(char) > ord(word):
                char = word

    res += char
    ans += min_v

print(res.rstrip())
print(ans)