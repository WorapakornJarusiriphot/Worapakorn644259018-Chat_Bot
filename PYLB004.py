import random
from flask import Flask
from linebot import LineBotApi, WebhookHandler

# สร้างแอปพลิเคชัน Flask
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # โค้ดที่ใช้จัดการ Webhook request
    return "OK", 200

def init(secret, token):
    # Initialization code
    pass

# กำหนดตัวแปร line_bot_api และ handler
line_bot_api = None
handler = None

# ฟังก์ชัน init เพื่อกำหนดค่าให้ line_bot_api และ handler
def init(secret, token):
    global line_bot_api, handler
    line_bot_api = LineBotApi(token)
    handler = WebhookHandler(secret)

#  0     1      2      3     4     5
color = ["แดง", "เขียว", "น้ำเงิน", "เหลือง", "ดำ", "ขาว"]
print("color =", color)
print(len(color))  # 6
                     
idx = random.randint(0, len(color) - 1)  # สุ่ม 0 ถึง 5(6-1)
print("idx =", idx)  #3
print(color[idx])

# กำหนดเส้นทาง (route) เริ่มต้น
@app.route('/')
def home():
    return f"Color selected: {color[idx]}"
