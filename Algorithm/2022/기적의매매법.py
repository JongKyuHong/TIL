money = int(input())
days = list(map(int, input().split()))

def bnf(money):
    stock = 0
    for day in days:
        if money >= day:
            stock += money // day 
            money = money % day
    return [stock, money]
stock1, money1 = bnf(money)
Jun = stock1*days[-1] + money1

def TIMING(money):
    down, up, standard, stock  = 0, 0, 0, 0
    for i in range(len(days)):
        if i == 0:
            standard = days[i]

        if standard < days[i]:
            up += 1
            down = 0
        elif standard > days[i]:
            down += 1
            up = 0
        else:
            down = 0
            up = 0
        if up >= 3:
            money += stock * days[i]
            stock = 0
        if down >= 3:
            stock += money // days[i]
            money = money % days[i]
        standard = days[i]
    return [stock, money]

stock2, money2 = TIMING(money)
Sung = stock2*days[-1] + money2

if Jun > Sung:
    print("BNP")
elif Sung > Jun:
    print("TIMING")
else:
    print("SAMESAME")
            
        