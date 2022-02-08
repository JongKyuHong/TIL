n, m = map(int, input().split())
s = set(input() for _ in range(n))
res = 0

for _ in range(m):
    word = input()
    if word in s:
        res += 1
print(res)