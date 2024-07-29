from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage,
                            StickerMessage,
                            ImageMessage,
                            LocationMessage,
                            VideoMessage, # mp4
                            AudioMessage) # m4a, mp3

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
    text_out = "คุณส่งข้อความเข้ามา"
    print(event)
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=text_out))

@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    text_out = "คุณส่งสติ๊กเกอร์เข้ามา"
    print(event)
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=text_out))
    
@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    text_out = "คุณส่งรูปภาพเข้ามา"
    print(event)
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=text_out))
    
@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    text_out = "คุณส่งตำแหน่งที่ตั้งเข้ามา"
    print(event.message.address)
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=text_out))

@handler.add(MessageEvent, message=VideoMessage)
def handle_video_message(event):
    text_out = "คุณส่งไฟล์วิดีโอเข้ามา"
    print(event)
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=text_out))

@handler.add(MessageEvent, message=AudioMessage)
def handle_audio_message(event):
    text_out = "คุณส่งไฟล์เสียงเข้ามา"
    print(event)
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=text_out))

if __name__ == "__main__":          
    app.run()

