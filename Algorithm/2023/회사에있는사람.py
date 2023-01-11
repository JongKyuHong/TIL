import sys 
input = sys.stdin.readline

n = int(input())
lst = {}
for _ in range(n):
    name, state = input().rstrip().split()
    if state == 'enter':
        lst[name] = 1
    else:
        del lst[name]
    
for k, v in sorted(lst.items(), reverse=True):
    print(k)
