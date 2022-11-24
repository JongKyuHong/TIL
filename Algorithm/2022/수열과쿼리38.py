import sys
input = sys.stdin.readline

m = int(input())
xor = 0
sum_v = 0
for i in range(m):
    data = input().rstrip().split()
    if data[0] == '1':
        xor = xor^int(data[1])
        sum_v += int(data[1])
    elif data[0] == '2':
        xor = xor^int(data[1])
        sum_v -= int(data[1])
    elif data[0] == '3':
        print(sum_v)
    else:
        print(xor)