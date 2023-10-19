import sys 
input = sys.stdin.readline

def check(x):
    sumx = 0
    for i in x:
        if i.isdigit():
            sumx += int(i)
    return sumx

N = int(input())
lst = []
for _ in range(N):
    input_ = input().rstrip()
    lst.append(input_)

lst.sort(key=lambda x: (len(x), check(x), x))
for value in lst:
    print(value) 