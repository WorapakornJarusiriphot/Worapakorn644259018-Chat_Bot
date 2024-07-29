from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TemplateSendMessage,
                            ConfirmTemplate,
                            MessageAction)

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
    
    if text == 'กาแฟ':
        ask_text = 'คุณต้องการดื่มกาแฟแบบใด'
        # กำหนดได้ไม่เกิน 2 ตัวเลือก เช่น Yes No หรือ ร้อน เย็น เป็นต้น
        confirm_template = ConfirmTemplate(text=ask_text,actions=[
            MessageAction(label='ร้อน', text='ขอสั่งกาแฟร้อน'),
            MessageAction(label='เย็น', text='ขอสั่งกาแฟเย็น')])
        
        template_message = TemplateSendMessage(alt_text="Hello",
                                               template=confirm_template)

        line_bot_api.reply_message(event.reply_token,template_message)
            
if __name__ == "__main__":          
    app.run()

