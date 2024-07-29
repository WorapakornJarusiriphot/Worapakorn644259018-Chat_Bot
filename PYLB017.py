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

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    print(text) 
                
    if (text.startswith("คำนวณ")): # "คำนวณ 4+6" 
        text_math = text.strip("คำนวณ").replace(" ", "") #--> " 4+6" --> "4+6"
        print(text_math)
        try:
            result = eval(text_math) # 10 --> "10"
            text_out = "เท่ากับ " + str(result)
            print(text_out)
            line_bot_api.reply_message(event.reply_token,
                                       TextSendMessage(text=text_out))
        except:
            pass
        
if __name__ == "__main__":          
    app.run()

