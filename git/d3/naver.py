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
        'price' : int(item['lprice']),
        'name' : item['title'],
        'link' : item['link']
    }
    return result
data =search_shopping('ps5')
print(data['price'],'hi')
res = f"{data['price']}"
if __name__ == '__main__':
    print(search_shopping('ps5'))