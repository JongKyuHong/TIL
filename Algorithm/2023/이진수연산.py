import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
result_and = ''
result_or = ''
result_xor = ''
result_not_a = ''
result_not_b = ''
for a, b in zip(A, B):
    if a == '1' and b == '1':
        result_and += '1'
    else:
        result_and += '0'
    if a == '1' or b == '1':
        result_or += '1'
    else:
        result_or += '0'
    if a != b:
        result_xor += '1'
    else:
        result_xor += '0'
    if a == '0':
        result_not_a += '1'
    else:
        result_not_a += '1'
    if b == '0':
        result_not_b += '1'
    else:
        result_not_b += '0'

print(result_and)
print(result_or)
print(result_xor)
print(result_not_a)
print(result_not_b)