import requests

url2 = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=NX8ua2F3RI56kEry2Utk6eYHrc3SUgluN41MamA42vYZVBb%2Bne2tpSfMdcmVG%2Bp%2FzgCY5qJchHr14M4Gg4x1BA%3D%3D&numOfRows=10&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0&returnType=json'
res2 = requests.get(url2)
data2 = res2.json()
# print(data2)
station1 = data2['response']['body']['items'][0]
mimun = station1['pm25Value']
name = station1['stationName']
print(f"{name}의 미세먼지는 수치는 {mimun} 입니다") 