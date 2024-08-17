from flask import Flask, request
from dotenv import load_dotenv
import os
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage

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
    except Exception as e:
        print(f"Error: {e}")
    
    return "Hello Line Chatbot"

ask_hello = ["สวัสดี","สวัสดีครับ","สวัสดีค่ะ","หวัดดี","ดี","ดีครับ"]
ask_name = ["ชื่ออะไร","คุณชื่ออะไร","ชื่ออะไรหรอ"]
ask_home = ["บ้านอยู่ที่ไหน","อยู่จังหวัดอะไร","บ้านอยู่ไหน"]

def handle_text_message(event):
    text = event.message.text
    print(text)
    
    if text in ask_hello:
        text_out = "สวัสดีครับ ยินดีที่ได้รู้จักนะครับ"
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text_out))
        
    elif text in ask_name:
        text_out = "ผมชื่อไลน์บอทครับ"
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text_out))

    elif text in ask_home:
        text_out = "บ้านอยู่ที่นครปฐมครับ"
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text_out))

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
