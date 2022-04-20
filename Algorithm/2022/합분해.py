n, k = map(int, input().split())
table = [1]
table += [0] * n

for _ in range(1, k+1):
    for idx in range(1, n+1):
        table[idx] = (table[idx] + table[idx-1]) % 1000000000

print(str(table[n]))

