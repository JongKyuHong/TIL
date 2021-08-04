import requests
from pprint import pprint
class TMDBHelper:

    
    #key='d7e0d2da76f5cfba5a78092d57b61d24'
    def __init__(self, api_key=None):
        self.api_key = api_key
    
    def get_request_url(self,method='/movie/popular',**kwargs):
        base_url = 'https://api.themoviedb.org/3'
        request_url = base_url+method
        request_url += f'?api_key={self.api_key}'
        for k,v in kwargs.items():
            request_url += f'&{k}={v}'
        return request_url

    def get_movie_id(self,title):
        request_url = self.get_request_url('/search/movie', query=title,region='KR',language='ko')
        # 검색결과 dict
        data = requests.get(request_url).json()
        results = data.get('results')
        if results:
            movie_id = results[0]['id']
            return movie_id
        else:
            return None


tmdb_helper = TMDBHelper('d7e0d2da76f5cfba5a78092d57b61d24')
tmdb_helper.get_request_url(language='ko',region='KR')
print(tmdb_helper.get_movie_id('기생충'))



d_.py
th = TMDBHelper('d7e0d2da76f5cfba5a78092d57b61d24')
movid_id = th.get_movie_id(title)
url = th.get_request_url(f'/movie/{movie_id}')....
requests.get(url)
추천영화 목록에
get_request_url 여기에 f스트링을 써서id를넣어요!


def popular_count():
    tmdb = TMDBHelper('d7e0d2da76f5cfba5a78092d57b61d24')
    url = tmdb.get_request_url('/movie/popluar',region='KR',language='ko')
    data = requests.get(url).json()
    popluar_movies = data[].... #여기는 답
    pprint(data)




