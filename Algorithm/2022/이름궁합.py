import string
uppers = list(string.ascii_uppercase)
numbers = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1,
           2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
stroke = dict(zip(uppers, numbers)) # 딕트집 입갤 A:3 이런식으로 매핑
me = input()
her = input()
me_t = list(me) # 격자? 느낌으로 문자열 넣기위해서 만듦
her_t = list(her)
name = [] # 이름 격자로 입력
score = [] # 점수 격자로 입력

length = len(me+her)

for i in range(length):
    if i % 2 == 0:
        name.append(me_t.pop(0)) # 내이름 그녀이름 격자로 넣어주기
    else:
        name.append(her_t.pop(0))

for i in name:
    score.append(stroke[i]) # 이름 점수 매핑


while length != 2:
    now = []
    for i in range(length-1): # 배열 길이를 점점 줄여가면서 반복함
        now.append((score[i] + score[i + 1]) % 10)
    length -= 1
    score = now # now로 계산하고 score 에 넣음
now = map(str, now)
print("".join(now))