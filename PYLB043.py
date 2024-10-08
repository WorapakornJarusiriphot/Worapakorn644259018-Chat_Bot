from flask import Flask, request ,send_from_directory
from dotenv import load_dotenv
import os 
from werkzeug.middleware.proxy_fix import ProxyFix
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage,
                            AudioSendMessage)
import os
from gtts import gTTS

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
        print('sopon')
        pass
    
    return "Hello Line Chatbot"


def handle_text_message(event):
    text = event.message.text
    print(text)

    speak = gTTS(text=text, lang='th')
    static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp').replace("\\","/")
    filename_image = 'speak.mp3'
    speak.save(static_tmp_path+'/'+filename_image) #บันทึกไฟล์เสียงลงห้อง tmp
             
    audio_url = request.host_url + os.path.join('static', 'tmp', filename_image).replace("\\","/")
    print(audio_url)
    audio_message = AudioSendMessage(
        original_content_url=audio_url,
        duration=15000) #15วินาที

    text_out = "แปลงข้อความเป็นเสียงพูดเรียบร้อยแล้ว"
    line_bot_api.reply_message(event.reply_token,
                               [TextSendMessage(text=text_out),
                                audio_message])
    
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

