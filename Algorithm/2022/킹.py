import sys
input = sys.stdin.readline

king, rock, n = input().rstrip().split()

r, c = 8-int(king[1]), ord(king[0])-65
r1, c1 = 8-int(rock[1]), ord(rock[0])-65

def check(r, c):
    if 0 <= r < 8 and 0 <= c < 8:
        return 1
    else:
        return 0

for _ in range(int(n)):
    move = input().rstrip()
    if move == 'R':
        c += 1
        if check(r, c):
            if r == r1 and c == c1:
                c1 += 1
                if not check(r1, c1):
                    c1 -= 1
                    c -= 1
        else:
            c -= 1
    elif move == 'L':
        c -= 1
        if check(r, c):
            if r == r1 and c == c1:
                c1 -= 1
                if not check(r1, c1):
                    c1 += 1
                    c += 1
        else:
            c += 1
    elif move == 'B':
        r += 1
        if check(r, c):
            if r == r1 and c == c1:
                r1 += 1
                if not check(r1, c1):
                    r1 -= 1
                    r -= 1
        else:
            r -= 1
    elif move == 'T':
        r -= 1
        if check(r, c):
            if r == r1 and c == c1:
                r1 -= 1
                if not check(r1, c1):
                    r1 += 1
                    r += 1
        else:
            r += 1
    elif move == 'RT':
        r -= 1
        c += 1
        if check(r, c):
            if r == r1 and c == c1:
                r1 -= 1
                c1 += 1
                if not check(r1, c1):
                    r1 += 1
                    c1 -= 1
                    r += 1
                    c -= 1
        else:
            r += 1
            c -= 1
    elif move == 'LT':
        r, c = r-1, c-1
        if check(r, c):
            if r == r1 and c == c1:
                r1 -= 1
                c1 -= 1
                if not check(r1, c1):
                    r1 += 1
                    c1 += 1
                    r += 1
                    c += 1
        else:
            r += 1
            c += 1
    elif move == 'RB':
        r, c = r+1, c+1
        if check(r, c):
            if r == r1 and c == c1:
                r1 += 1
                c1 += 1
                if not check(r1, c1):
                    r1 -= 1
                    c1 -= 1
                    r -= 1
                    c -= 1
        else:
            r -= 1
            c -= 1
    elif move == 'LB':
        r, c = r+1, c-1
        if check(r, c):
            if r == r1 and c == c1:
                r1 += 1
                c1 -= 1
                if not check(r1, c1):
                    r1 -= 1
                    c1 += 1
                    r -= 1
                    c += 1
        else:
            r -= 1
            c += 1

king = str(chr(c+65))+str(8-r)
rock = str(chr(c1+65))+str(8-r1)
print(king)
print(rock)