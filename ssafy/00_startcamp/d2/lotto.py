import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=971'
res = requests.get(url)
data = res.json()

print(data.text)

