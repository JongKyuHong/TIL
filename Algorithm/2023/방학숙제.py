L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

A_v = 0
B_c = 0
if A % C == 0:
    A_v = A//C
else:
    A_v = A//C+1

if B % D == 0:
    B_v = B//D
else:
    B_v = B//D+1
print(L-max(A_v, B_v))