from collections import deque
import sys
import math
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(2)
    print(3)
    print(5)
    print(7)
    exit()
    
res = []

def is_prime_number(x):
    for j in range(2, int(math.sqrt(x)+1)):
        if x % j == 0:
            return 0
    return 1

def dfs(nums):
    global res
    for i in range(1,len(nums)+1):
        t = is_prime_number(int(nums[:i]))
        if not t:
            return
    if len(nums) == n:
        res.append(nums)
        return
    for i in range(1, 10):
        dfs(nums+str(i))

for i in ['2','3','5','7']:
    dfs(i)

for i in res:
    print(i)