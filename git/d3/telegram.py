import requests
import naver
# url = f'https://api.telegram.org/bot{token}/getMe'
#Update 현황 받아보기
# getupdate = f'https://api.telegram.org/bot{token}/getUpdates'
# f'https://api.telegram.org/bot{token}/setWebhook?url=우리서버URL'
# 메시지보내기
# f'https://api.telegram.org/bot{token}/setWebhook?url=https://eba63247c2fa.ngrok.io/recieve'
token = '1832532680:AAHarOjYwH4RWotTo7GkooMA549pJYSXAsU'
chat_id = '1895576493'

def send_message(chat_id,message):
    token = '1832532680:AAHarOjYwH4RWotTo7GkooMA549pJYSXAsU'
    #chat_id = '1895576493'
    
    url = f'https://api.telegram.org/bot{token}/sendMessage?text={message}&chat_id={chat_id}'
    requests.get(url).json()
if __name__ == '__main__':
    #print(send_message('hi'))
    print(f'https://api.telegram.org/bot{token}/setWebhook?url=https://16c633979ce4.ngrok.io/recieve')
# 1. f'https://api.telegram.org/bot{token}/setWebhook?url=https://eba63247c2fa.ngrok.io/recieve'을 완성후 브라우저 => 엔터
# 2. 텔레그램 봇에게 메시지 보내기
# 3. 서버 로그(터미널)에서 메시지 확인
