token = '1832532680:AAHarOjYwH4RWotTo7GkooMA549pJYSXAsU'
chat_id = '1895576493'
getme = f'https://api.telegram.org/bot{token}/getMe'
getUpdates = f'https://api.telegram.org/bot{token}/getUpdates'
sendMessage = f'https://api.telegram.org/bot{token}/sendMessage?text=안녕하세요&chat_id={chat_id}'

print(sendMessage)