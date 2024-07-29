from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage,
                            AudioSendMessage)
import os
from gtts import gTTS
import GT

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
        print('sopon')
        pass
    
    return "Hello Line Chatbot"

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    print(text)

    text_en = GT.translate(text,'th','en') # th --> en
    print(text_en)
    
    speak = gTTS(text=text_en, lang='en')
    static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp').replace("\\","/")
    filename_image = 'speak.mp3'
    speak.save(static_tmp_path+'/'+filename_image) #บันทึกไฟล์เสียงลงห้อง tmp
    print('Done')
             
    audio_url = request.host_url + os.path.join('static', 'tmp', filename_image).replace("\\","/")
    print(audio_url)
    audio_message = AudioSendMessage(
        original_content_url=audio_url,
        duration=15000)

    text_out = "แปลงข้อความเป็นเสียงพูด เรียบร้อยแล้ว"
    line_bot_api.reply_message(event.reply_token,
                               [TextSendMessage(text=text_en),
                                TextSendMessage(text=text_out),
                                audio_message])
    
@app.route('/static/<path:path>')
def send_static_content(path):
    return send_from_directory('static', path)

if __name__ == "__main__":          
    app.run()

