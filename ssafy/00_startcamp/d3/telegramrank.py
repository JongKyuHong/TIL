import requests
from bs4 import BeautifulSoup
from datetime import datetime
def search_rank():
    token = '1832532680:AAHarOjYwH4RWotTo7GkooMA549pJYSXAsU'
    
    url = 'https://qwer.gg/leagues/LCK/2021/summer'
    res = requests.get(url)
    data = BeautifulSoup(res.text,'html.parser')
    a = []
    for i in range(1,11):
        rank = data.select_one(f'#root > div.Ads > div:nth-child(2) > div > div.League__tournament > div > section.Tournament__sections > section:nth-child(2) > div.Tabs > div.Tabs__contents > div > table.BorderedTable.RankTable.Ranks--desktop > tbody > tr:nth-child({i}) > td.RankTable__rank.Gilroy')
        name = data.select_one(f'#root > div.Ads > div:nth-child(2) > div > div.League__tournament > div > section.Tournament__sections > section:nth-child(2) > div.Tabs > div.Tabs__contents > div > table.BorderedTable.RankTable.Ranks--desktop > tbody > tr:nth-child({i}) > td.RankTable__name.Gilroy')
        rate = data.select_one(f'#root > div.Ads > div:nth-child(2) > div > div.League__tournament > div > section.Tournament__sections > section:nth-child(2) > div.Tabs > div.Tabs__contents > div > table.BorderedTable.RankTable.Ranks--desktop > tbody > tr:nth-child({i}) > td:nth-child(4) > div')                        
       
        if len(name.text) == 6:
            a.append(name.text[:3])
        else:
            a.append(name.text[:2])
        a.append(rank.text)
        a.append(rate.text)
        #print(f'현재 {name.text}팀이 {rate.text}의 스코어로 {rank.text}등입니다.')
    
    link = 'https://qwer.gg/schedules/'+str(datetime.today().strftime("%Y-%m"))
    return a, link

if __name__ == '__main__':
    print(search_rank())

