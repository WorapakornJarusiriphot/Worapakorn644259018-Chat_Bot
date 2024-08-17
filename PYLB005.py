from flask import Flask, request
from dotenv import load_dotenv
import os
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage)

import random

line_bot_api = None
handler = None

def init(secret, token):
    global line_bot_api, handler
    line_bot_api = LineBotApi(token)
    handler = WebhookHandler(secret)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    try:
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)
        handler.handle(body, signature)
    except:
        pass
    
    return "Hello Line Chatbot"

ask_hello = ["สวัสดี","สวัสดีครับ","สวัสดีค่ะ","หวัดดี"]
ask_name = ["ชื่ออะไร","คุณชื่ออะไร","ชื่ออะไรหรอ"]
ask_home = ["บ้านอยู่ที่ไหน","อยู่แถวไหน"]

answer_hello = ["ยินดีที่ได้รู้จัก","สวัสดีนะ","หวัดดีเพื่อนใหม่"]
answer_name = ["ผมชื่อไลน์บอทครับ","ไลน์บอท","ชื่อไลน์บอทครับผม"]
answer_home = ["อยู่ในใจเธอ","บ้านอยู่ใกล้เซเว่น","นครปฐม","จังหวัดนครปฐม"]


def handle_text_message(event):
    text = event.message.text
    print(text)
    
    if text in ask_hello:
        idx = random.randint(0,len(answer_hello)-1) # สุ่ม 0 ถึง 2(3-1)
        text_out = answer_hello[idx]
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))
        
    if text in ask_name:
        idx = random.randint(0,len(answer_name)-1) # สุ่ม 0 ถึง 2(3-1)
        text_out = answer_name[idx]
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))

    if text in ask_home:
        idx = random.randint(0,len(answer_home)-1) # สุ่ม 0 ถึง 3(4-1)
        text_out = answer_home[idx]
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))


def setup_handler():
    handler.add(MessageEvent, message=TextMessage)(handle_text_message)

if __name__ == "__main__":
    # โหลดตัวแปรจาก .env
    load_dotenv()
    channel_secret = os.getenv("CHANNEL_SECRET")
    channel_access_token = os.getenv("CHANNEL_ACCESS_TOKEN")
    
    init(channel_secret, channel_access_token)
    setup_handler()
    app.run()

