from flask import Flask
import GT

# สร้างแอป Flask
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # โค้ดที่ใช้จัดการ Webhook request
    return "OK", 200

def init(secret, token):
    # Initialization code
    pass

# เรียกใช้ไลบรารี googletrans สำหรับการแปลภาษา
@app.route('/')
def home():
    text_th = 'สวัสดีครับ ผมเป็นนักเรียน'
    print(text_th)

    text_en = GT.translate(text_th,'th','en') # th --> en
    print(text_en)
    return "Translation completed."

# ฟังก์ชัน init สำหรับ main.py
def init(secret, token):
    pass  # ถ้าไม่มีอะไรต้องตั้งค่าใน init ก็ใส่ pass ไว้
