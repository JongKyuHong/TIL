n , m = map(int,input().split())

if n == 1 or m == 1:
    cnt = 1
elif m >= 7:
    if n >= 3 : cnt = (m-6)+4
elif m in (4,5,6):
    if n>=3 : cnt=4
    else : cnt = (m+1)//2
elif m in (2,3):
    if n>=3: cnt=m
    else: cnt=(m+1)//2
print(cnt)