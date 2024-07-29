from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage)

channel_secret = "bd64f7ffb48f1aada1527ee852c4fda0"
channel_access_token = "RrewYzqHmm7KSmeVPPowpWx44BrF1ABUhMxaFvb2wwPlLf/Ct6M0w+mQpZBOkTt5RxwtW0jUmT97K1JTKn7vW968Qdgo3btfXw425HYFsaanXy/YcqXSRMePK8r4pdCi6b6GkoSNfTQz8guUo69iuAdB04t89/1O/w1cDnyilFU="

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

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

ask_hello = ["สวัสดี","สวัสดีครับ","สวัสดีค่ะ","หวัดดี","ดี","ดีครับ"]
ask_name = ["ชื่ออะไร","คุณชื่ออะไร","ชื่ออะไรหรอ"]
ask_home = ["บ้านอยู่ที่ไหน","อยู่จังหวัดอะไร","บ้านอยู่ไหน"]

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    print(text)
    
    if text in ask_hello:
        text_out = "สวัสดีครับ ยินดีที่ได้รู้จักนะครับ"
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))
        
    if text in ask_name:
        text_out = "ผมชื่อไลน์บอทครับ"
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))

    if text in ask_home:
        text_out = "บ้านอยู่ที่นครปฐมครับ"
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text_out))

if __name__ == "__main__":          
    app.run()

