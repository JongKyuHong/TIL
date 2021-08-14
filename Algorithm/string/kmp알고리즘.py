def kmpSearch(H,N):
    n = len(H)  # 문자열의 크기
    m = len(N)  # 패턴의 크기
    ret = []
    pi = getPartialMatch(N)  # 패턴을 넘겨준다

    begin = 0
    matched = 0
    while begin <= n-m:
        if matched < m and H[begin+matched] == N[matched]:
            matched += 1
            if matched == m:
                ret.append(begin)
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched-pi[matched-1]
                matched = pi[matched-1]
    return ret

def getPartialMatch(N):
    m = len(N)  # 패턴의 길이
    pi = [0] * m  # pi는 패턴의 길이만큼 0으로 초기화한 리스트
    begin = 1  # 시작위치 1
    matched = 0  # 일치한 문자열 0
    while begin + matched < m:  # 시작위치와 일치한 문자열의 갯수의 합이 패턴의 길이보다 작으면
        if N[begin+matched] == N[matched]:  # 시작위치+일치한 문자열 만큼 간곳과 일치한 문자열 만큼 간곳이 같으면
            matched += 1  # 일치한 문자열 길이 1증가
            pi[begin + matched - 1] = matched  # 시작위치 + 일치한 문자열 -1 에 일치한 문자열 크기 넣는다.
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi

H = "aflkjsklfaabaabacdsfwdsfaba"  # 해당 문자열
N = "aabaabac"  # 찾을 패턴
print(kmpSearch(H, N))
