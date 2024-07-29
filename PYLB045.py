import google.generativeai as genai

genai.configure(api_key="xxx")

model = genai.GenerativeModel("gemini-pro")

prompt = "ร่างจดหมายลาพักผ่อน ไปเที่ยวเซนทรัลนครปฐม วันที่ 9 เมษายน 2567"
print("prompt : ",prompt)

try:
    response = model.generate_content(prompt)
    print(response.text)
except:
    print("no response")
    


