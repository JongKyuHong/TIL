N = int(input())
numbers = [input() for _ in range(N)]
i = 1
while 1:
    if len(set(map(lambda x: x[-i:], numbers))) == N:
        print(i)
        break
    i += 1