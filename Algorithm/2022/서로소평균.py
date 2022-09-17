N = int(input())
A = list(map(int, input().split()))
X = int(input())
res = []
def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def lcm(a,b):
    return a*b // gcd(a,b)

for i in A:
    cnt = gcd(i, X)
    if cnt == 1:
        res.append(i)
print(sum(res)/len(res))