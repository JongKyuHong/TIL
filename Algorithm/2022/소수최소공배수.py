def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b // gcd(a,b)

n = int(input())
A = list(map(int, input().split()))
nums = [False, False] + [True] * (max(A)-1)
res = []
for i in range(2, max(A)+1):
    if nums[i]:
        if i in A:
            res.append(i)
        for j in range(2*i, max(A)+1, i):
            nums[j] = False

len_ = len(res)
if len_ > 0:
    idx = 0
    target = res[idx]
    while len_-1 > idx:
        target = lcm(target, res[idx+1])
        idx += 1

    print(target)
else:
    print(-1)


