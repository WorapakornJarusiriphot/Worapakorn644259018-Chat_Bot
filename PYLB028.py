from flask import Flask, request, send_from_directory  # แก้ไขการนำเข้าที่ถูกต้อง
from dotenv import load_dotenv
import os
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            FlexSendMessage,
                            BubbleContainer,
                            BoxComponent,
                            TextComponent,
                            BubbleStyle,
                            BlockStyle)

line_bot_api = None
handler = None

def init(secret, token):
    global line_bot_api, handler
    line_bot_api = LineBotApi(token)
    handler = WebhookHandler(secret)

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


def handle_text_message(event):
    text = event.message.text
    print(text)  
#---------------------------------------------------------------------------      
    if text == 'A': # มีครบ 4 ส่วน header, hero, body, footer
        flex = BubbleContainer(
            header = BoxComponent(layout='vertical',
                                  contents=[TextComponent(
                                      text='header',align='center')]),
            hero = BoxComponent(layout='vertical',
                                contents=[TextComponent(
                                    text='hero',align='center')]),
            body = BoxComponent(layout='vertical',
                                contents=[TextComponent(
                                    text='body',align='center')]),
            footer = BoxComponent(layout='vertical',
                                  contents=[TextComponent(
                                      text='footer',align='center')]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------
    if text == 'B': # มี 1 ส่วน body อย่างเดียว
        flex = BubbleContainer(
            body = BoxComponent(layout='vertical',
                                contents=[TextComponent(
                                    text='body',align='center')]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------
    if text == 'C': # การปรับขนาดของ BubbleContainer
        flex = BubbleContainer(
            size = 'micro', # nano,micro,kilo,*mega,giga
            body = BoxComponent(layout='vertical',
                                contents=[TextComponent(
                                    text='body',align='center')]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------
    if text == 'D': # การเปลี่ยนสีพื้นหลังของ body
        flex = BubbleContainer(
            size = 'micro', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#fffacb')),
            body = BoxComponent(layout='vertical',
                                contents=[TextComponent(
                                    text='body',align='center')]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------
    if text == 'E': # มีครบ 4 ส่วน และ การเปลี่ยนสีพื้นหลังของ header, hero, body, footer
        flex = BubbleContainer(
            size = 'micro', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(
                header=BlockStyle(background_color='#61bdac'),
                hero=BlockStyle(background_color='#416fec'),
                body=BlockStyle(background_color='#fffacb'),
                footer=BlockStyle(background_color='#ffe4e1')),
            header = BoxComponent(layout='vertical',
                                  contents=[TextComponent(
                                      text='header',align='center')]),
            hero = BoxComponent(layout='vertical',
                                contents=[TextComponent(
                                    text='hero',align='center')]),
            body = BoxComponent(layout='vertical',
                                contents=[TextComponent(
                                    text='body',align='center')]),
            footer = BoxComponent(layout='vertical',
                                  contents=[TextComponent(
                                      text='footer',align='center')]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------       

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

