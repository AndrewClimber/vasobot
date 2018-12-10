#!/usr/bin/python3.6

import requests as rq
import tele_ini
import yobit
from time import sleep


#import json

#====================================================================
TOKEN = tele_ini.telegram_api_token
URL = tele_ini.telegram_api_url + TOKEN + '/'
WEB_HOOK = tele_ini.telegram_api_url + TOKEN + '/'
#====================================================================
def set_webhook(webhook_url):
    rq.get(WEB_HOOK + 'setWebhook?url={}'.format(webhook_url))

#====================================================================
def get_updates():
    return rq.get(URL + 'getUpdates').json()
#====================================================================
def get_message():
    data = get_updates()
    return {'id': data['result'][-1]['message']['chat']['id'],
            'text': data['result'][-1]['message']['text'],
            'update_id': data['result'][-1]['update_id']
            }
#====================================================================
def send_message(chat_id, text='Who are you? I did not call you! Go to the dick!'):
    url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    rq.get(url)
#====================================================================
def q2a_translator(chat_id,text):
    text = text.strip().lower()
    if 'hi' in text:
        send_message(chat_id,'You a stupid!')
    elif '/btc' in text:
        send_message(chat_id, yobit.get_btc())
    elif '/help' in text:
        helps = """
/help - help
/stop - kill bot
/btc  - btc rate
        """
        send_message(chat_id, helps)
    elif '/stop' in text:
        send_message(chat_id,'You kill me, bastard !')
        print ("Content-type: text/html\n\n")
        print("<html>I'll be back.</html>")
        return False
    else:
        send_message(chat_id)
    return True
#====================================================================
def main():
    try:


    except Exception:
        print ("Content-type: text/html\n\n")
        print("<html>Any error.</html>")

    try:
        update_id = get_message()['update_id'];
        while True:
            answer = get_message()
            if update_id != answer['update_id']:
                update_id = answer['update_id']
                if q2a_translator(answer['id'], answer['text']) == False:
                    break
                sleep(3)
    except Exception:
        print ("Content-type: text/html\n\n")
        print("<html>Any error.</html>")
"""
    Nice json-output into file  !
    with open('updates.json','w') as f:
        json.dump(d,f, indent=2, ensure_ascii=False)
        """
#====================================================================
if __name__ == '__main__':
    main()
