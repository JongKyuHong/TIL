import sys
input = sys.stdin.readline

k = int(input())
k -= 1
a_cnt = 0
b_cnt = 1

while k:
    sum_cnt = a_cnt + b_cnt
    a_cnt = b_cnt
    b_cnt = sum_cnt
    k -= 1
print(a_cnt, b_cnt)

# 0 1
# 1 1
# 1 2
# 2 3 BABBA
# 3 5 BABBABAB
# 5 8 BABBABABBABBA

#바로 전 B갯수가 다음 A 
#바로전 A+B갯수가 다음 B