import sys
input = sys.stdin.readline

inp = input().rstrip()
n = len(inp)
idx = 0
ans = ''
while idx < n:
    if idx+4 <= n and inp[idx:idx+4] == 'XXXX':
        ans += 'AAAA'
        idx += 4
    elif idx+2 <= n and inp[idx:idx+2] == 'XX':
        ans += 'BB'
        idx += 2
    elif inp[idx] == '.':
        ans += '.'
        idx += 1
    else:
        print(-1)
        exit()

print(ans)