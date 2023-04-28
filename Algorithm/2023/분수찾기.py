import sys
input = sys.stdin.readline

X = int(input())

d = 1
num = 0
while num < X:
    num += d
    d += 1

if d % 2 == 0:
    molecule = 1
    denominator = d-1
    while 1:
        if num == X:
            print(f'{molecule}/{denominator}')
            break
        else:
            denominator -= 1
            molecule += 1
            num -= 1
else:
    molecule = d-1
    denominator = 1
    while 1:
        if num == X:
            print(f'{molecule}/{denominator}')
            break
        else:
            denominator += 1
            molecule -= 1
            num -= 1

# 1. X면 몇번째 행렬인지 확인
# 2. 그 행렬이면 어떤 분수가 들어있어야하는지 계산

# 1_1 인덱스상 짝수 인덱스 열인경우에 우로 이동 홀수 인덱스의 경우 아래로 이동

# 1 2 3 4 5  1씩 증가하는 등차수열
# d-1 행 혹은 열
# 14 기준 다섯번째 열이기 때문에 좌로 이동합니다. 네번째에서 다섯번째로 오니까 
# 이뜻은 분모부터 빼면서 진행된다
# 14기준으로 1/5부터 2/4 이런식으로 진행
