from flask import Flask

# สร้างแอป Flask
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # โค้ดที่ใช้จัดการ Webhook request
    return "OK", 200

def init(secret, token):
    # Initialization code
    pass

# ฟังก์ชัน init ที่ใช้ใน main.py
def init(secret, token):
    pass  # ถ้าไม่มีการตั้งค่าอะไรเพิ่มเติมให้ใช้ pass ไว้ก่อน

# โค้ดเดิมของคุณ
text = "คำนวณ 4+6"
print(text)

result = text.startswith("คำนวณ") # "คำนวณ 4+6" ใช่ True
print(result)

text_cut = text.strip("คำนวณ") # " 4+6"
print(text_cut)

text_cut = text_cut.replace(" ", "") # "4+6"
print(text_cut)
