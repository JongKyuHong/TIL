import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

len_s = len(s)
len_t = len(t)
len_sum = len_s * len_t
div_s = len_sum//len_s
div_t = len_sum//len_t

print(s * div_s)
print(t * div_t)
if s * div_s == t * div_t:
    print(1)
else:
    print(0)



