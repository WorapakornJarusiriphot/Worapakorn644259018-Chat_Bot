from flask import Flask, request, send_from_directory  # แก้ไขการนำเข้าที่ถูกต้อง
from dotenv import load_dotenv
import os
from werkzeug.middleware.proxy_fix import ProxyFix
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage,
                            ImageMessage,
                            ImageSendMessage)
import tempfile
import cv2

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

def handle_image_message(event):
    message_content = line_bot_api.get_message_content(event.message.id)
    static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp').replace("\\","/")
    print(static_tmp_path)
    
    with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix='jpg' + '-', delete=False) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)
        tempfile_path = tf.name
        
    dist_path = tempfile_path + '.jpg'
    os.rename(tempfile_path, dist_path)

    filename_image = os.path.basename(dist_path)
    filename_fullpath = dist_path.replace("\\","/")
    
    img = cv2.imread(filename_fullpath)

    # ใส่โค้ดประมวลผลภาพตรงส่วนนี้
    img_out = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cv2.imwrite(filename_fullpath, img_out)
    
    dip_url = request.host_url + os.path.join('static', 'tmp', filename_image).replace("\\","/")
    print(dip_url)
    line_bot_api.reply_message(
        event.reply_token, [
            TextSendMessage(text='ประมวลผลภาพเรียบร้อยแล้ว'),
            ImageSendMessage(dip_url, dip_url)])
    
@app.route('/static/<path:path>')
def send_static_content(path):
    return send_from_directory('static', path)

def setup_handler():
    handler.add(MessageEvent, message=TextMessage)(handle_text_message)
    handler.add(MessageEvent, message=ImageMessage)(handle_image_message)

if __name__ == "__main__":
    # โหลดตัวแปรจาก .env
    load_dotenv()
    channel_secret = os.getenv("CHANNEL_SECRET")
    channel_access_token = os.getenv("CHANNEL_ACCESS_TOKEN")
    
    init(channel_secret, channel_access_token)
    setup_handler()
          
    app.run()
