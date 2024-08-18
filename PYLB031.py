from flask import Flask, request, send_from_directory  # แก้ไขการนำเข้าที่ถูกต้อง
from dotenv import load_dotenv
import os
from werkzeug.middleware.proxy_fix import ProxyFix
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            FlexSendMessage,
                            BubbleContainer,
                            BoxComponent,
                            ImageComponent,
                            MessageAction)

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

    img_url_1 = request.url_root + '/static/cake1.png'
    img_url_2 = request.url_root + '/static/cake2.png'
    img_url_3 = request.url_root + '/static/cake3.png'
    img_url_4 = request.url_root + '/static/cake4.png'

    #img_url_1 = 'https://cdn.pixabay.com/photo/2020/12/17/10/18/cheesecake-5838905_960_720.jpg'
    #img_url_2 = 'https://cdn.pixabay.com/photo/2014/11/28/08/03/brownie-548591_960_720.jpg'
    #img_url_3 = 'https://cdn.pixabay.com/photo/2018/03/20/21/46/food-3244824_960_720.jpg'
    #img_url_4 = 'https://cdn.pixabay.com/photo/2019/04/02/17/07/tiramisu-4098241_960_720.jpg'

#---------------------------------------------------------------------------     
    if text == 'A': # มี image 1 อัน
        flex = BubbleContainer(
            size = 'micro', # nano,micro,kilo,*mega,giga
            hero = BoxComponent(
                layout='vertical',
                contents=[ImageComponent(url=img_url_1,
                                         size='full',
                                         action=MessageAction(text='ชีสเค้กมิกซ์เบอรี่')
                                         )]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------     
    if text == 'B': # มี image 1 อัน
        flex = BubbleContainer(
            size = 'kilo', # nano,micro,kilo,*mega,giga
            hero = BoxComponent(
                layout='vertical',
                contents=[ImageComponent(url=img_url_1,
                                         size='full',
                                         action=MessageAction(text='ชีสเค้กมิกซ์เบอรี่')
                                         )]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)

#---------------------------------------------------------------------------     
    if text == 'C': # มี image 2 อัน แนวตั้ง
        flex = BubbleContainer(
            size = 'kilo', # nano,micro,kilo,*mega,giga
            hero = BoxComponent(
                layout='vertical',
                contents=[ImageComponent(url=img_url_1,
                                         size='full',
                                         action=MessageAction(text='ชีสเค้กมิกซ์เบอรี่')
                                         ),
                          ImageComponent(url=img_url_2,
                                         size='full',
                                         action=MessageAction(text='บราวนี่')
                                         )]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)

#---------------------------------------------------------------------------     
    if text == 'D': # มี image 2 อัน แนวนอน
        flex = BubbleContainer(
            size = 'kilo', # nano,micro,kilo,*mega,giga
            hero = BoxComponent(
                layout='horizontal',
                contents=[ImageComponent(url=img_url_1,
                                         size='full',
                                         action=MessageAction(text='ชีสเค้กมิกซ์เบอรี่')
                                         ),
                          ImageComponent(url=img_url_2,
                                         size='full',
                                         action=MessageAction(text='บราวนี่')
                                         )]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#---------------------------------------------------------------------------     
    if text == 'E': # มี image 4 อัน
        flex = BubbleContainer(
            size = 'kilo', # nano,micro,kilo,*mega,giga
            hero = BoxComponent(
                layout='vertical',
                contents=[BoxComponent(
                    layout='horizontal',
                    contents=[ImageComponent(url=img_url_1,
                                         size='full',
                                         action=MessageAction(text='ชีสเค้กมิกซ์เบอรี่')
                                         ),
                          ImageComponent(url=img_url_2,
                                         size='full',
                                         action=MessageAction(text='บราวนี่')
                                         )]),
                          BoxComponent(
                    layout='horizontal',
                    contents=[ImageComponent(url=img_url_3,
                                         size='full',
                                         action=MessageAction(text='เค้กมะม่วง')
                                         ),
                          ImageComponent(url=img_url_4,
                                         size='full',
                                         action=MessageAction(text='เค้กทีรามิสุ')
                                         )])]))        
        flex_message = FlexSendMessage(alt_text='Hello',contents=flex)
        line_bot_api.reply_message(event.reply_token,flex_message)
#--------------------------------------------------------------------------- 
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

