import requests
import os
from dotenv import load_dotenv

load_dotenv()

def send_to_telegram(message):


    apiToken = os.environ["TELEGRAM_API_TOKEN"]
    chatID = os.environ["CHAT_ID_CHADI"]
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

send_to_telegram("Test elak chadi")