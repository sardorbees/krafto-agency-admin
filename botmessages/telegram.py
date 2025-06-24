import requests

TELEGRAM_BOT_TOKEN = '7614226832:AAGUGKTBy0J5HpBj9Pyuh4uUIco2GTmWADE'
TELEGRAM_CHAT_ID = '7139975148'

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': text,
        'parse_mode': 'HTML'
    }
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
    except Exception as e:
        print('Ошибка при отправке в Telegram:', e)
