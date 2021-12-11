def gcd(x,y):
    while y > 0:
        x,y = y, x%y
    return x

def div(x):
    div_list = [x]
    for i in range(2, int(x**(1/2)+1)):
        if x % i == 0:
            div_list.append(i)
            if x//i != i:
                div_list.append(x//i)
    div_list.sort()
    return div_list

n = int(input())
array = [int(input()) for _ in range(n)]
array.sort(reverse=True)

diff = []
for i in range(n-1):
    diff.append(array[i] - array[i+1])

if len(diff) == 1:
    answer = diff[0]
elif len(diff) == 2:
    answer = gcd(diff[0], diff[1])
else:
    answer = diff[0]
    for i in range(1, len(diff)):
        answer = gcd(answer, diff[i])
for i in div(answer):
    print(i, end=' ')
