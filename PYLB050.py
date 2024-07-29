from flask import Flask, request, send_from_directory
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

channel_secret = "bd64f7ffb48f1aada1527ee852c4fda0"
channel_access_token = "RrewYzqHmm7KSmeVPPowpWx44BrF1ABUhMxaFvb2wwPlLf/Ct6M0w+mQpZBOkTt5RxwtW0jUmT97K1JTKn7vW968Qdgo3btfXw425HYFsaanXy/YcqXSRMePK8r4pdCi6b6GkoSNfTQz8guUo69iuAdB04t89/1O/w1cDnyilFU="

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

app = Flask(__name__)
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

@handler.add(MessageEvent, message=TextMessage)
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

if __name__ == "__main__":          
    app.run()

