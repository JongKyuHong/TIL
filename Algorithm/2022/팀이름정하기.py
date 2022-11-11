import sys 
input = sys.stdin.readline

yundo = list(input().rstrip())
n = int(input())
res = 0
result = []

for _ in range(n):
    data = input().rstrip()
    lcount = yundo.count('L')
    ocount = yundo.count('O')
    vcount = yundo.count('V')
    ecount = yundo.count('E')
    for i in data:
        if i == 'L':
            lcount += 1
        elif i == 'O':
            ocount += 1
        elif i == 'V':
            vcount += 1
        elif i == 'E':
            ecount += 1
    ans = ((lcount+ocount)*(lcount+vcount)*(lcount+ecount)*(ocount+vcount)*(ocount+ecount)*(vcount+ecount)) % 100
    if ans > res:
        res = ans
        result = [data]
    elif ans == res:
        result.append(data)

result.sort()
print(result[0])