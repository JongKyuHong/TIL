import sys
input = sys.stdin.readline

while 1:
    a, b = map(int, input().split())
    if not a and not b:
        break
    print('Yes' if a > b else 'No')
