import requests


def search_shopping(keyword):
    url = f'https://openapi.naver.com/v1/search/shop.json?query={keyword}'

    naver_client_id = '0OXZsVTvv2wNpI1AfPeN'
    naver_client_secret = 'ZOd14KTMiQ'

    h = {
        'X-Naver-Client-Id':naver_client_id,
        'X-Naver-Client-Secret':naver_client_secret
    }

    res = requests.get(url, headers=h).json()
    item = res['items'][0]
    result = {
        'price': int(item['lprice']),
        'name': item['title'],
        'link': item['link'],
    }
    return result

def send_message(me):
    token = '1832532680:AAHarOjYwH4RWotTo7GkooMA549pJYSXAsU'
    chat_id = '1895576493'
    #me = '최저가는 : ' + lprice
    #al = list(input("원하는 최저가 목록을 입력해주세요 ").split(''))

    url = f'https://api.telegram.org/bot{token}/sendMessage?text={me}&chat_id={chat_id}'
    requests.get(url).json()

data2 = search_shopping('ps5')
msg = f"{data2['name']}의 가격은 {data2['price']:,}원. \n{data2['link']}"
send_message(msg)