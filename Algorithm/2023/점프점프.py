x,y,p1,p2 = map(int,input().split())
runx = set(range(p1, 10**6, x))
runy = set(range(p2, 10**6, y))

R = runx&runy
print(min(R) if R else -1)