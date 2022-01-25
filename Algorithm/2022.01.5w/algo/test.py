n = int(input())
count = {'0' : 0, '1' : 0}
for _ in range(n):
    a = int(input())
    count[str(a)] += 1
print(max(count))