import sys
input = sys.stdin.readline

cards = list(range(1,21))
for _ in range(10):
    a, b = map(int, input().split()) # 
    lst = cards[a-1:b]
    idx = len(lst)-1
    for i in range(a-1, b):
        cards[i] = lst[idx]
        idx -= 1
print(*cards)