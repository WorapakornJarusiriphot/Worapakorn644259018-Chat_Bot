from flask import Flask, request, send_from_directory
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            FlexSendMessage,
                            BubbleContainer,
                            BoxComponent,
                            TextComponent,
                            BubbleStyle,
                            BlockStyle)

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
if __name__ == "__main__":          
    app.run()

