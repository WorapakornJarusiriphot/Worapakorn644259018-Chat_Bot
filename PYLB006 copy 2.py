import os
from wit import Wit
from dotenv import load_dotenv

# โหลดตัวแปรจากไฟล์ .env
load_dotenv()

# ดึงค่า WIT_ACCESS_TOKEN จากไฟล์ .env
wit_access_token = os.getenv("WIT_ACCESS_TOKEN")

# สร้าง client ของ Wit.ai
client = Wit(wit_access_token)

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
