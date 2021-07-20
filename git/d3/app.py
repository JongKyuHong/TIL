from flask import Flask,request
import naver
import telegram
import telegramrank


app = Flask(__name__)

"할 수 있는 일 을 정의한다 => "
@app.route('/')
def index():
    print(request.host)
    return 'Hello!!'

@app.route('/recieve',methods=['POST'])
def recieve():
    data = request.get_json()
    data2,link2 = telegramrank.search_rank()
    chat_id = data['message']['chat']['id']
    msg = data['message']['text']
    if msg == '하이':
        telegram.send_message(chat_id,'하이')
    elif msg == 'lck' or msg == 'LCK':
        for i in range(0,len(data2),3):
            telegram.send_message(chat_id,f'현재 {data2[i]}팀이 {data2[i+2]}의 승-패로 {data2[i+1]}등 입니다.')
        telegram.send_message(chat_id,f'경기일정 보러가기 : {link2}')
    else:
        telegram.send_message(chat_id,':(  다른건 몰라잉')
    #telegram.send_message(chat_id,msg)
    return 'ok', 200

@app.route('/send')
def send():
    data = naver.search_shopping('ps5')

    msg = f"{data['name']}의 가격은 {data['price']:,}원. \n{data['link']}"
    telegram.send_message(msg)    
    return 'OK'

if __name__ =='__main__':
    app.run(debug=True)

