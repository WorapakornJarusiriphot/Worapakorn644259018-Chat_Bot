from flask import Flask, request
from dotenv import load_dotenv
import os
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage)

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

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    print(text)
    #print(event)
    
    if text == "สวัสดี":
        text_out = "ยินดีที่ได้รู้จักครับ"
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))
        #line_bot_api.push_message("xxxxxxx",
        #                           TextSendMessage(text=text_out))
                
    if text == "ชื่ออะไร":
        text_out = "สายฟ้าครับ"
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))

if __name__ == "__main__":
    # โหลดตัวแปรจาก .env
    load_dotenv()
    channel_secret = os.getenv("CHANNEL_SECRET")
    channel_access_token = os.getenv("CHANNEL_ACCESS_TOKEN")
    
    init(channel_secret, channel_access_token)
    setup_handler()
          
    app.run()

