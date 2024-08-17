from flask import Flask, request
from dotenv import load_dotenv
import os
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage,
                            StickerMessage,
                            ImageMessage,
                            LocationMessage,
                            VideoMessage,
                            AudioMessage)

line_bot_api = None
handler = None

def init(secret, token):
    global line_bot_api, handler
    line_bot_api = LineBotApi(token)
    handler = WebhookHandler(secret)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
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
    text_out = "คุณส่งข้อความเข้ามา"
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=text_out))

def handle_sticker_message(event):
    text_out = "คุณส่งสติ๊กเกอร์เข้ามา"
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=text_out))

def handle_image_message(event):
    text_out = "คุณส่งรูปภาพเข้ามา"
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=text_out))

def handle_location_message(event):
    text_out = "คุณส่งตำแหน่งที่ตั้งเข้ามา"
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=text_out))

def handle_video_message(event):
    text_out = "คุณส่งไฟล์วิดีโอเข้ามา"
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=text_out))

def handle_audio_message(event):
    text_out = "คุณส่งไฟล์เสียงเข้ามา"
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=text_out))

def setup_handler():
    handler.add(MessageEvent, message=TextMessage)(handle_text_message)
    handler.add(MessageEvent, message=StickerMessage)(handle_sticker_message)
    handler.add(MessageEvent, message=ImageMessage)(handle_image_message)
    handler.add(MessageEvent, message=LocationMessage)(handle_location_message)
    handler.add(MessageEvent, message=VideoMessage)(handle_video_message)
    handler.add(MessageEvent, message=AudioMessage)(handle_audio_message)

if __name__ == "__main__":
    # โหลดตัวแปรจาก .env
    load_dotenv()
    channel_secret = os.getenv("CHANNEL_SECRET")
    channel_access_token = os.getenv("CHANNEL_ACCESS_TOKEN")

    init(channel_secret, channel_access_token)
    setup_handler()

    app.run()
