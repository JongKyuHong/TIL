import sys
input = sys.stdin.readline

n = input().rstrip()
n_len = len(n)
lines = ['.','.','#','.','.']

for i in range(n_len):
    if (i+1)%3 != 0:
        lines[0] += '.#.'
        lines[1] += '#.#'
        lines[2] += f'.{n[i]}.'
        lines[3] += '#.#'
        lines[4] += '.#.'
    else:
        lines[0] += '..*..'
        lines[1] += '.*.*.'
        lines[2] += f'*.{n[i]}.*'
        lines[3] += '.*.*.'
        lines[4] += '..*..'
    
    if (i+1) % 3 == 1:
        lines[0] += '.'
        lines[1] += '.'
        lines[2] += '#'
        lines[3] += '.'
        lines[4] += '.'

if n_len % 3 == 2:
    lines[0] += '.'
    lines[1] += '.'
    lines[2] += '#'
    lines[3] += '.'
    lines[4] += '.'

for line in lines:
    print(line)