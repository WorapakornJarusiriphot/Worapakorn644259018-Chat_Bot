from flask import Flask, request, send_from_directory  # แก้ไขการนำเข้าที่ถูกต้อง
from dotenv import load_dotenv
import os
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage)

from openpyxl import load_workbook
import time

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

    dt = time.localtime()
    DD = '{:02d}'.format(dt[2]) + '/' + '{:02d}'.format(dt[1]) + '/' + str(dt[0])
    TT = '{:02d}'.format(dt[3]) + ':' + '{:02d}'.format(dt[4]) + ':' + '{:02d}'.format(dt[5])
    print(DD)
    print(TT)

    xlsx_filename='log.xlsx'
    wb = load_workbook(xlsx_filename)
    ws = wb['Sheet1']
    ws.append([DD,TT,text])
    wb.save(xlsx_filename)
    
    text_out = "บันทึกข้อความเรียบร้อย"
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))
    

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

