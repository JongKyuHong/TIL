p = 'is'
t = 'This is a book~!'
m = len(p)
n = len(t)

def bruteforce(p,t):
    i = 0  # t의 인덱스
    j = 0  # p의 인덱스
    while j < m and j < n:
        if t[i] != p[j]:
            i = i - j  # 비교를 시작한 위치
            j = -1  # 초기화
        i += 1  # 이전비교한곳 다음위치
        j += 1
    if j == m: return i -m  # 검색 성공
    else: return -1  # 검색 실패