import sys
input = sys.stdin.readline

def recur(string, n):
    if n == 0:
        return '-'
    ans = ''
    len_string = len(string)
    for i in range(3):
        if i == 1:
            ans += ' '*(len_string//3)
        else:
            ans += recur(string[i*(len_string//3):(i+1)*(len_string//3)], n-1)
    return ans
while 1:
    try:
        N = int(input())
        string = '-'*(3**N)
        if N == 0:
            print(string)
            continue
        ans = recur(string, N)
        print(ans)
    except:
        break