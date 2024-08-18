from flask import Flask, request
from dotenv import load_dotenv
import os
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage,
                            StickerSendMessage)

from wit import Wit

line_bot_api = None
handler = None

wit_access_token = "xxx"
client = Wit(wit_access_token)

def init(secret, token):
    global line_bot_api, handler
    line_bot_api = LineBotApi(token)
    handler = WebhookHandler(secret)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # โค้ดที่ใช้จัดการ Webhook request
    return "OK", 200

def init(secret, token):
    # Initialization code
    pass

@app.route("/", methods=["GET","POST"])
def home():
    try:
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)
        handler.handle(body, signature)
    except:
        pass
    
    return "Hello Line Chatbot"


def handle_text_message(event):
    text = event.message.text
    print(text)
    
    if (text != ""):
        ret = client.message(text)
        if len(ret["intents"]) > 0:
            confidence = ret["intents"][0]['confidence']
            
            if (confidence > 0.8):
                intents_name = ret["intents"][0]['name']        
                print("intent = ",intents_name)

                if (intents_name=="greeting"):
                    p_id = 446
                    s_id = 1989
                    line_bot_api.reply_message(event.reply_token,
                                               StickerSendMessage(package_id=p_id,
                                                                  sticker_id=s_id))
                   
                if (intents_name=="weather"):
                    p_id = 789
                    s_id = 10892
                    line_bot_api.reply_message(event.reply_token,
                                               StickerSendMessage(package_id=p_id,
                                                                  sticker_id=s_id))
                               
                if (intents_name=="date"):
                    p_id = 11537
                    s_id = 52002759
                    line_bot_api.reply_message(event.reply_token,
                                               StickerSendMessage(package_id=p_id,
                                                                  sticker_id=s_id))
                    
                if (intents_name=="joke"):
                    p_id = 11539
                    s_id = 52114116
                    line_bot_api.reply_message(event.reply_token,
                                               StickerSendMessage(package_id=p_id,
                                                                  sticker_id=s_id))
                    
            else:
                print("intent = unknow")
                text_out = "ฉันไม่เข้าใจสิ่งที่คุณถาม กรุณาถามใหม่อีกครั้ง"
                line_bot_api.reply_message(event.reply_token,
                                           TextSendMessage(text=text_out))
        else:
            print("intent = unknow")
            text_out = "ฉันไม่เข้าใจสิ่งที่คุณถาม กรุณาถามใหม่อีกครั้ง"
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

