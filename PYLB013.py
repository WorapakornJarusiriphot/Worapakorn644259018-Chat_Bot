from flask import Flask
import GT

# สร้างแอป Flask
app = Flask(__name__)

# เรียกใช้ไลบรารี googletrans สำหรับการแปลภาษา
@app.route('/')
def translate_text():
    text_en = 'There are four cats on the table.'
    print(text_en)

    text_th = GT.translate(text_en, 'en', 'th')  # en --> th
    print(text_th)
    return f'Translation: {text_th}'

# ฟังก์ชัน init ที่ใช้ใน main.py
def init(secret, token):
    pass  # ถ้าไม่มีการตั้งค่าอะไรเพิ่มเติมให้ใช้ pass ไว้ก่อน
