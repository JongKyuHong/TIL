import sys
input = sys.stdin.readline

# 홀수의 갯수 적음
# 수가 한자리면 종료
# 수가 두자리면 2개로 나눠서 합을 구하여 새로운 수 생각
# 수가 세자리 이상이면 임의의 위치에서 끊어서 3개의 수로 분할하고, 3개를 더한 값을 새로운수로 생각
def check(string):
    cnt = 0
    for i in string:
        if int(i) % 2:
            cnt += 1
    return cnt


def find(string, cnt):
    global max_v, min_v
    n = len(string)
    cnt += check(string)

    #print(string, cnt) 514 2
    if n == 1: # 크기가 1인경우에 내가 무엇인지 확인하고 종료
        min_v = min(min_v, cnt)
        max_v = max(max_v, cnt)
        return
    if n == 2:
        ans = int(string[0]) + int(string[1])
        ans = str(ans)
        find(ans, cnt)
    else:
        for i in range(1, n-1):
            for j in range(i+1, n):
                ans = int(string[:i]) + int(string[i:j]) + int(string[j:])
                find(str(ans), cnt)

S = input().rstrip()
min_v, max_v = sys.maxsize, 0
find(S, 0)
print(min_v, max_v)