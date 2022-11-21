import sys 
input = sys.stdin.readline
n = int(input())
lst = input()
value = 0
tmp = '' 
for i in lst:
    if i.isdigit():
        tmp += i
    else:
        value += int(tmp)
        tmp = ''
        
print(value-(n*(n-1)//2))