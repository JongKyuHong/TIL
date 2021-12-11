n = int(input())

ti = list(map(int,input().split()))
ti.sort(reverse=True)
result = 0
for index,value in enumerate(ti):
    result = max(result,index+value+2)
print(result)