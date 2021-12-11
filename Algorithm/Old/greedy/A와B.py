# s = input()
# t = input() #처음은 그냥 박치기
# def check1(str):
#     return str[::-1]+'B'
# def check2(str):
#     return str+'A'

# chance = len(t)-len(s)
# word = s  #바꿀그거를 저장
# while chance > 0:
#     for i in range(chance):
#         print(word)
#         word = check1(word)
#         print(word,'첫번째 변환후')
#     for i in range(chance,len(t)-len(s)):
#         word = check2(word)
#         print(word,'두번째 변환후')
#     if word == t:
#         print(1)
#         break
#     else:
#         word = s
#     chance -= 1
# if word !=t :
#     print(0)


#------------ 둘째시도는 뒤에서 부터 뺴는걸로
s = input()
t = input()

def check1(str):
    str = str[:len(str)-1]
    return str[::-1]
def check2(str):
    return str[:len(str)-1]
length = len(t)
while len(t) > len(s):
    if t[-1] == 'B':
        t = check1(t)
    elif t[-1] == 'A':
        t = check2(t)
if t == s:
    print(1)
else:
    print(0)
# a = 'asdf'
# print(a[:len(a)-1])