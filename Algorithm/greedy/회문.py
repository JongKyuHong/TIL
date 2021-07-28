n = int(input())
flag = 0
goal = 0
for _ in range(n):
    text = input()
    text = list(text)
    if len(text)%2 == 0:
        if text[:(len(text)//2)] == text[(len(text)//2):][::-1]:
            print(0)
        else:
            print(2)    
    else:
        fron = []
        tier = []
        fron.append(text.pop(0))
        tier.append(text.pop(-1))
        while len(text) >= 2:
            if fron[-1] != tier[-1]:
                fron.append(text.pop(0))
                tier.append(text.pop(-1))
                print(fron)
                print(tier)
                if fron[-1] == tier[-2] or fron[-2] == tier[-1]:
                    print(1)
                    goal = 1
                else:
                    print(2)
                    goal = 1
            else:
                continue
        if goal == 0:
            print(1)
        goal = 0
            

# *2는 무조건 짝수다 ,, 즉슨 하나가 삐져나온경우는 무조건 홀수일수밖에 없다.
# 양쪽에서 다가가면서 하나씩 넣고 그게 다른경우 바로앞에 있는 원소를 서로 교차해서 확인했는데 같으면 유사회문 아니면 2