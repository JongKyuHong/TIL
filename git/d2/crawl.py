import requests
from bs4 import BeautifulSoup
url = 'https://finance.naver.com/sise/'

res = requests.get(url)
data = BeautifulSoup(res.text,'html.parser') 

kospi = data.select_one('#KOSPI_now')

print(kospi.text)

url2 = 'https://finance.naver.com/marketindex/'
res2 = requests.get(url2)
data2 = BeautifulSoup(res2.text,'html.parser')
dollar = data2.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print(dollar.text)