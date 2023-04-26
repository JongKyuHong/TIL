import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    A.sort()
    B.sort()
    max_a_value = max(A)
    idx = 0
    for i in range(len(A)):
        gap = max_a_value
        tmp = 0
        tmp_idx = 0
        for j in range(idx, len(B)):
            if abs(A[i] - B[j]) < gap:
                gap = abs(A[i]-B[j])
                tmp = B[j]
                tmp_idx = j
            elif abs(A[i]-B[j]) == gap:
                if tmp > B[j]:
                    tmp = B[j]
                    tmp_idx = j
            else:
                break
        C.append(tmp)
        idx = tmp_idx
    print(sum(C))
                
