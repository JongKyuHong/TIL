import sys
input = sys.stdin.readline

k = int(input())
idx = 0
while 1:
    if 2**idx > k:
        idx -=1
        break
    idx +=1
print(idx)
k -= 2**idx
print(k)
nums = '4'*idx
print(nums)
    
