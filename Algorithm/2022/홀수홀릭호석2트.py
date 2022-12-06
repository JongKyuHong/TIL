import sys
input = sys.stdin.readline

n = input().rstrip()
max_ans = -1
min_ans = float('inf')
def find(n, ans):
    len_n = len(n)
    if len_n == 1:
        if int(n) % 2:
            ans += 1
        global max_ans, min_ans
        max_ans = max(max_ans, ans)
        min_ans = min(min_ans, ans)
        return
    elif len_n == 2:
        if int(n[0]) % 2:
            ans += 1
        if int(n[1]) % 2:
            ans += 1
        find(str(int(n[0])+int(n[1])), ans)
    else:
        for i in n:
            if int(i) % 2:
                ans += 1
        for i in range(1, len_n-1):
            for j in range(i+1, len_n):
                find(str(int(n[:i]) + int(n[i:j]) + int(n[j:])), ans)


find(n, 0)
print(min_ans, max_ans)