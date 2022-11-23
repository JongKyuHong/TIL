import sys
input = sys.stdin.readline

n, m = map(int, input().split())
if n == 0:
    print(0)
    exit()
books = list(map(int, input().split()))

box = m
ans = 1
for book in books:
    if box >= book:
        box -= book
    else:
        ans += 1
        box = m-book
print(ans)