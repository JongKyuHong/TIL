for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    li = li + li[0]
    print(li)