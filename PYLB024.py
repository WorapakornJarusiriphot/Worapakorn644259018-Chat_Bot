from flask import Flask, request
from dotenv import load_dotenv
import os
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TemplateSendMessage,
                            ConfirmTemplate,
                            MessageAction)

line_bot_api = None
handler = None

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
    
    if text == 'กาแฟ':
        ask_text = 'คุณต้องการดื่มกาแฟแบบใด'
        # กำหนดได้แค่ 2 ทางเลือก เช่น Yes No หรือ ร้อน เย็น เป็นต้น
        confirm_template = ConfirmTemplate(text=ask_text,actions=[
            MessageAction(label='ร้อน', text='กาแฟร้อน'),
            MessageAction(label='เย็น', text='กาแฟเย็น')])
        
        template_message = TemplateSendMessage(alt_text="Hello",
                                               template=confirm_template)
        line_bot_api.reply_message(event.reply_token,template_message)

    if text == 'กาแฟร้อน':
        ask_text = 'คุณต้องการรับ size ใด'        
        confirm_template = ConfirmTemplate(text=ask_text,actions=[
            MessageAction(label='แก้วเล็ก', text='คุณสั่งกาแฟร้อนแก้วเล็ก'),
            MessageAction(label='แก้วใหญ่', text='คุณสั่งกาแฟร้อนแก้วใหญ่')])
        
        template_message = TemplateSendMessage(alt_text="Hello",
                                               template=confirm_template)
        line_bot_api.reply_message(event.reply_token,template_message)

    if text == 'กาแฟเย็น':
        ask_text = 'คุณต้องการความหวานแบบใด'
        confirm_template = ConfirmTemplate(text=ask_text,actions=[
            MessageAction(label='หวานปกติ', text='คุณสั่งกาแฟเย็นหวานปกติ'),
            MessageAction(label='หวานน้อย', text='คุณสั่งกาแฟเย็นหวานน้อย')])
        
        template_message = TemplateSendMessage(alt_text="Hello",
                                               template=confirm_template)
        line_bot_api.reply_message(event.reply_token,template_message)


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

