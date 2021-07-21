r,g,b = map(int,input().split())
result = (((r*g*b/8)/1024)/1024)
print('{:.2f}'.format(result), "MB")