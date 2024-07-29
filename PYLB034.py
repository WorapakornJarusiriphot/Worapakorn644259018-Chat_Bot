from flask import Flask, request, send_from_directory
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage)

from openpyxl import load_workbook
import time

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
    
if __name__ == "__main__":          
    app.run()

