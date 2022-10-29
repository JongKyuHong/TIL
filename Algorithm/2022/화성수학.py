import sys
input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip().split()
    ans = float(data[0])
    for i in range(1, len(data)):
        if data[i] == '@':
            ans *= 3
        elif data[i] == '%':
            ans += 5
        elif data[i] == '#':
            ans -= 7
    print('%0.2f' % ans)