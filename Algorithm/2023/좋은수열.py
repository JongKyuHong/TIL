import sys
input = sys.stdin.readline

def check(string): # 수열 검사
    if string[-2] == string[-1]:
        return 0
    else:
        for i in range(2, len(string)//2 + 1):
            #print(string, i, string[-(i*2):-i], string[-i:],'check')
            if string[-(i*2):-i] == string[-i:]:
                return 0
    return 1

def makestring(string):
    if len(string) == N:
        global ans
        print(string)
        exit()
    if len(string) % 2 == 0:
        if check(string + '1'):
            makestring(string+'1')
        if check(string + '2'):
            makestring(string+'2')
        if check(string+'3'):
            makestring(string+'3')
    else:
        if check(string + '1'):
            makestring(string+'1')
        elif check(string + '2'):
            makestring(string+'2')
        elif check(string+'3'):
            makestring(string+'3')

N = int(input())
ans = ''
makestring('1')

# 아마 앞에서부터 차근차근 푸는 문제인것같음 그리디추정
# 좋은수열만 이어붙여서 만든다
# 좋은수열을 만드려면 같은수 연속 x, 패턴 연속 x인데
# 같은수 연속 x는 조건문으로 편하게 만들 수 있지만, 패턴 연속의 경우는..?
# 백트래킹은 어떨까 싶다.
# 새로운 수열을 만들었을때 검사하는 내용 있으면 될듯??
# 1 2 3중 하나를 넣고 검증해서 ㅇㅋ면 넘어간다..? 