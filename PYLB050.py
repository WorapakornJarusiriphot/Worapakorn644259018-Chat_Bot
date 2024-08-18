from flask import Flask, request, send_from_directory  # แก้ไขการนำเข้าที่ถูกต้อง
from dotenv import load_dotenv
import os
from werkzeug.middleware.proxy_fix import ProxyFix
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage,
                            ImageSendMessage)

import GT
import cv2
from stability_ai import text2image
api_key   = "xxx"
engine_id = "stable-diffusion-v1-6"
filename_save = "/static/tmp/image_temp.jpg"

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
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_proto=1)

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
    
    prompt_text_th = text
    prompt_text_en = GT.translate(prompt_text_th,'th','en') # th --> en
    print(prompt_text_en)

    try:
        text2image(api_key,engine_id,prompt_text_en,filename_save)
        dip_url = request.host_url + filename_save
        print(dip_url)
        
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=prompt_text_en),
                TextSendMessage(text='ประมวลผลภาพเรียบร้อยแล้ว'),
                ImageSendMessage(dip_url,dip_url)])
    except:
        print("no response")
    
@app.route('/static/<path:path>')
def send_static_content(path):
    return send_from_directory('static', path)


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

