import os
from wit import Wit
from dotenv import load_dotenv
from flask import Flask

# โหลดตัวแปรจากไฟล์ .env
load_dotenv()

# ดึงค่า WIT_ACCESS_TOKEN จากไฟล์ .env
wit_access_token = os.getenv("WIT_ACCESS_TOKEN")

# สร้าง client ของ Wit.ai
client = Wit(wit_access_token)

# สร้างแอปพลิเคชัน Flask
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # โค้ดที่ใช้จัดการ Webhook request
    return "OK", 200

def init(secret, token):
    # Initialization code
    pass

def init(secret, token):
    """ ฟังก์ชัน init เพื่อให้สอดคล้องกับการเรียกใช้ใน main.py """
    global client
    client = Wit(token)
    print(f"Initialized with token: {token}")

# ตัวอย่างข้อความที่จะส่งไปให้ Wit.ai
text = "สวัสดีครับ"
#text = "วันนี้วันอะไรกันนะ"
#text = "ขอมุกตลก"
#text = "ขอเปิดไฟหน่อย"

print("text = ",text)

if text != "":
    # ส่งข้อความไปยัง Wit.ai และรับ response กลับมา
    ret = client.message(text)
    if len(ret["intents"]) > 0:
        confidence = ret["intents"][0]['confidence']
        
        if confidence > 0.8:
            intents_name = ret["intents"][0]['name']        
            print("intent = ",intents_name)
        else:
            print("intent = unknow")
    else:
        print("intent = unknow")

# เส้นทางเริ่มต้นสำหรับ Flask
@app.route('/')
def home():
    return "Wit.ai integration with Flask is running."
