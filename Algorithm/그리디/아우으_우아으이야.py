n = int(input())
x,y = map(int,input().split())

result = 0

for i in range(n-1):
    xx, yy = map(int,input().split())
    if xx == x:
        y = yy
    elif y>=xx and yy>y:
        y = yy
    elif y < xx:
        result += abs(x-y)
        x = xx
        y = yy
print(result + abs(y-x))