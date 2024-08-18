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
                            BlockStyle,
                            CarouselContainer,
                            ImageComponent,
                            MessageAction,
                            ButtonComponent)

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
    if text == 'A': # มีข้อความเดียว
        flex1 = BubbleContainer(
            size = 'micro', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#fffacb')),
            body = BoxComponent(
                layout='vertical',
                contents=[TextComponent(text='สวัสดีครับ',
                                        align='center', # *start,end,center
                                        color='#0000ff',
                                        weight='regular', # *regular,bold
                                        style='italic', # *normal, italic
                                        decoration='none', # *none,underline,line-through
                                        size='xl' # xxs,xs,sm,*md,lg,xl,xxl,3xl,4xl,5xl
                                        )]))
        
        flex2 = BubbleContainer(
            size = 'micro', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#eeeeee')),
            body = BoxComponent(
                layout='vertical',
                contents=[TextComponent(text='เลือกเค้ก',
                                        align='center', # *start,end,center
                                        color='#0000ff',
                                        weight='regular', # *regular,bold
                                        style='italic', # *normal, italic
                                        decoration='none', # *none,underline,line-through
                                        size='xl' # xxs,xs,sm,*md,lg,xl,xxl,3xl,4xl,5xl
                                        ),
                          ButtonComponent(style='primary', # primary,secondary,link
                                          color='#ffc181',
                                          margin = 'md',
                                          action=MessageAction(
                                              label='ส้ม',
                                              text='คุณสั่งเค้กส้ม')),
                          ButtonComponent(style='primary', # primary,secondary,link
                                          color='#f0d020',
                                          margin = 'md',
                                          action=MessageAction(
                                              label='กล้วยหอม',
                                              text='คุณสั่งเค้กกล้วยหอม'))]))

        flex3 = BubbleContainer(
            size = 'micro', # nano,micro,kilo,*mega,giga
            styles = BubbleStyle(body=BlockStyle(background_color='#fff2f4')),
            body = BoxComponent(
                layout='vertical',
                contents=[TextComponent(text='เลือกกาแฟ',
                                        align='center', # *start,end,center
                                        color='#0000ff',
                                        weight='regular', # *regular,bold
                                        style='italic', # *normal, italic
                                        decoration='none', # *none,underline,line-through
                                        size='xl' # xxs,xs,sm,*md,lg,xl,xxl,3xl,4xl,5xl
                                        ),
                          ButtonComponent(style='primary', # primary,secondary,link
                                          color='#cc4668',
                                          margin = 'md',
                                          action=MessageAction(
                                              label='ร้อน',
                                              text='คุณสั่งกาแฟร้อน')),
                          ButtonComponent(style='primary', # primary,secondary,link
                                          color='#61bdac',
                                          margin = 'md',
                                          action=MessageAction(
                                              label='เย็น',
                                              text='คุณสั่งกาแฟเย็น'))]))

        flex4 = BubbleContainer(
            size = 'micro', 
            hero = BoxComponent(
                layout='vertical',
                contents=[ImageComponent(url='https://cdn.pixabay.com/photo/2017/08/21/09/03/background-2664549_960_720.jpg',
                                         size='full',
                                         action=MessageAction(text='ดอกไม้')
                                         )]))        
        
        carousel = CarouselContainer(contents=[flex1,flex2,flex3,flex4]) # max=12อัน
            
        flex_message = FlexSendMessage(alt_text='Hello',contents=carousel)
        line_bot_api.reply_message(event.reply_token,flex_message)


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

