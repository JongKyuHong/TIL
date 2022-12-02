import sys 
input = sys.stdin.readline

lst = list(map(int, input().split()))
lst2 = sorted(lst)

while lst != lst2:
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            print(*lst)