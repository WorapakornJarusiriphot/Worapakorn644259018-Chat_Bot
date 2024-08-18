import multiprocessing  # เพิ่มบรรทัดนี้
from multiprocessing import Process
from dotenv import load_dotenv
import os
import PYLB001
import PYLB002
import PYLB003
import PYLB004
import PYLB005
import PYLB006
import PYLB007
import PYLB008
import PYLB009
import PYLB010
import PYLB011
import PYLB012
import PYLB013
import PYLB014
import PYLB015
import PYLB016
import PYLB017
import PYLB018
import PYLB019
import PYLB020
import PYLB021
import PYLB022
import PYLB023
import PYLB024
import PYLB025
import PYLB026
import PYLB027
import PYLB028
import PYLB029
import PYLB030
import PYLB031
import PYLB032
import PYLB033
import PYLB034
import PYLB035
import PYLB036
import PYLB037
import PYLB038
import PYLB039
import PYLB040
import PYLB041
import PYLB042
import PYLB043
import PYLB044
import PYLB045
import PYLB046
import PYLB047
import PYLB048
import PYLB049
import PYLB050
import PYLB051
import stability_ai
import yolo_predictions

# โหลดตัวแปรจากไฟล์ .env
load_dotenv()

channel_secret = os.getenv("CHANNEL_SECRET")
channel_access_token = os.getenv("CHANNEL_ACCESS_TOKEN")

# Move Flask app initialization here to the global scope
app1 = PYLB001.app
app2 = PYLB002.app
app3 = PYLB003.app
app4 = PYLB004.app
app5 = PYLB005.app
app6 = PYLB006.app
app7 = PYLB007.app
app8 = PYLB008.app
app9 = PYLB009.app
app10 = PYLB010.app
app11 = PYLB011.app
app12 = PYLB012.app
app13 = PYLB013.app
app14 = PYLB014.app
app15 = PYLB015.app
# app16 = PYLB016.app
app17 = PYLB017.app
app18 = PYLB018.app
# app19 = PYLB019.app
# app20 = PYLB020.app
app21 = PYLB021.app
app22 = PYLB022.app
app23 = PYLB023.app
app24 = PYLB024.app
app25 = PYLB025.app
app26 = PYLB026.app
app27 = PYLB027.app
app28 = PYLB028.app
app29 = PYLB029.app
app30 = PYLB030.app
app31 = PYLB031.app
app32 = PYLB032.app
app33 = PYLB033.app
app34 = PYLB034.app
app35 = PYLB035.app
app36 = PYLB036.app
app37 = PYLB037.app
app38 = PYLB038.app
app39 = PYLB039.app
app40 = PYLB040.app
app41 = PYLB041.app
# app42 = PYLB042.app
app43 = PYLB043.app
app44 = PYLB044.app
# app45 = PYLB045.app
# app46 = PYLB046.app
app47 = PYLB047.app
app48 = PYLB048.app
# app49 = PYLB049.app
app50 = PYLB050.app
app51 = PYLB051.app

def run_flask_app(app, init_func, secret, token, port):
    init_func(secret, token)  # เรียก init เพื่อกำหนดค่า line_bot_api และ handler
    app.run(port=port)

def main():
    processes = []  # สร้าง list สำหรับเก็บ process

    processes.append(Process(target=run_flask_app, args=(app1, PYLB001.init, channel_secret, channel_access_token, 5001)))
    processes.append(Process(target=run_flask_app, args=(app2, PYLB002.init, channel_secret, channel_access_token, 5002)))
    processes.append(Process(target=run_flask_app, args=(app3, PYLB003.init, channel_secret, channel_access_token, 5003)))
    # processes.append(Process(target=run_flask_app, args=(app4, PYLB004.init, channel_secret, channel_access_token, 5004)))
    processes.append(Process(target=run_flask_app, args=(app5, PYLB005.init, channel_secret, channel_access_token, 5005)))
    # processes.append(Process(target=run_flask_app, args=(app6, PYLB006.init, channel_secret, channel_access_token, 5006)))
    processes.append(Process(target=run_flask_app, args=(app7, PYLB007.init, channel_secret, channel_access_token, 5007)))
    processes.append(Process(target=run_flask_app, args=(app8, PYLB008.init, channel_secret, channel_access_token, 5008)))
    processes.append(Process(target=run_flask_app, args=(app9, PYLB009.init, channel_secret, channel_access_token, 5009)))
    processes.append(Process(target=run_flask_app, args=(app10, PYLB010.init, channel_secret, channel_access_token, 5010)))
    # processes.append(Process(target=run_flask_app, args=(app11, PYLB011.init, channel_secret, channel_access_token, 5011)))
    processes.append(Process(target=run_flask_app, args=(app12, PYLB012.init, channel_secret, channel_access_token, 5012)))
    # processes.append(Process(target=run_flask_app, args=(app13, PYLB013.init, channel_secret, channel_access_token, 5013)))
    processes.append(Process(target=run_flask_app, args=(app14, PYLB014.init, channel_secret, channel_access_token, 5014)))
    # processes.append(Process(target=run_flask_app, args=(app15, PYLB015.init, channel_secret, channel_access_token, 5015)))
    # processes.append(Process(target=run_flask_app, args=(app16, PYLB016.init, channel_secret, channel_access_token, 5016)))
    processes.append(Process(target=run_flask_app, args=(app17, PYLB017.init, channel_secret, channel_access_token, 5017)))
    processes.append(Process(target=run_flask_app, args=(app18, PYLB018.init, channel_secret, channel_access_token, 5018)))
    # processes.append(Process(target=run_flask_app, args=(app19, PYLB019.init, channel_secret, channel_access_token, 5019)))
    # processes.append(Process(target=run_flask_app, args=(app20, PYLB020.init, channel_secret, channel_access_token, 5020)))
    processes.append(Process(target=run_flask_app, args=(app21, PYLB021.init, channel_secret, channel_access_token, 5021)))
    processes.append(Process(target=run_flask_app, args=(app22, PYLB022.init, channel_secret, channel_access_token, 5022)))
    processes.append(Process(target=run_flask_app, args=(app23, PYLB023.init, channel_secret, channel_access_token, 5023)))
    processes.append(Process(target=run_flask_app, args=(app24, PYLB024.init, channel_secret, channel_access_token, 5024)))
    processes.append(Process(target=run_flask_app, args=(app25, PYLB025.init, channel_secret, channel_access_token, 5025)))
    processes.append(Process(target=run_flask_app, args=(app26, PYLB026.init, channel_secret, channel_access_token, 5026)))
    processes.append(Process(target=run_flask_app, args=(app27, PYLB027.init, channel_secret, channel_access_token, 5027)))
    processes.append(Process(target=run_flask_app, args=(app28, PYLB028.init, channel_secret, channel_access_token, 5028)))
    processes.append(Process(target=run_flask_app, args=(app29, PYLB029.init, channel_secret, channel_access_token, 5029)))
    processes.append(Process(target=run_flask_app, args=(app30, PYLB030.init, channel_secret, channel_access_token, 5030)))
    processes.append(Process(target=run_flask_app, args=(app31, PYLB031.init, channel_secret, channel_access_token, 5031)))
    processes.append(Process(target=run_flask_app, args=(app32, PYLB032.init, channel_secret, channel_access_token, 5032)))
    processes.append(Process(target=run_flask_app, args=(app33, PYLB033.init, channel_secret, channel_access_token, 5033)))
    processes.append(Process(target=run_flask_app, args=(app34, PYLB034.init, channel_secret, channel_access_token, 5034)))
    processes.append(Process(target=run_flask_app, args=(app35, PYLB035.init, channel_secret, channel_access_token, 5035)))
    processes.append(Process(target=run_flask_app, args=(app36, PYLB036.init, channel_secret, channel_access_token, 5036)))
    processes.append(Process(target=run_flask_app, args=(app37, PYLB037.init, channel_secret, channel_access_token, 5037)))
    processes.append(Process(target=run_flask_app, args=(app38, PYLB038.init, channel_secret, channel_access_token, 5038)))
    processes.append(Process(target=run_flask_app, args=(app39, PYLB039.init, channel_secret, channel_access_token, 5039)))
    processes.append(Process(target=run_flask_app, args=(app40, PYLB040.init, channel_secret, channel_access_token, 5040)))
    processes.append(Process(target=run_flask_app, args=(app41, PYLB041.init, channel_secret, channel_access_token, 5041)))
    # processes.append(Process(target=run_flask_app, args=(app42, PYLB042.init, channel_secret, channel_access_token, 5042)))
    processes.append(Process(target=run_flask_app, args=(app43, PYLB043.init, channel_secret, channel_access_token, 5043)))
    processes.append(Process(target=run_flask_app, args=(app44, PYLB044.init, channel_secret, channel_access_token, 5044)))
    # processes.append(Process(target=run_flask_app, args=(app45, PYLB045.init, channel_secret, channel_access_token, 5045)))
    # processes.append(Process(target=run_flask_app, args=(app46, PYLB046.init, channel_secret, channel_access_token, 5046)))
    processes.append(Process(target=run_flask_app, args=(app47, PYLB047.init, channel_secret, channel_access_token, 5047)))
    processes.append(Process(target=run_flask_app, args=(app48, PYLB048.init, channel_secret, channel_access_token, 5048)))
    # processes.append(Process(target=run_flask_app, args=(app49, PYLB049.init, channel_secret, channel_access_token, 5049)))
    processes.append(Process(target=run_flask_app, args=(app50, PYLB050.init, channel_secret, channel_access_token, 5050)))
    processes.append(Process(target=run_flask_app, args=(app51, PYLB051.init, channel_secret, channel_access_token, 5051)))

    # เริ่มกระบวนการในแต่ละ process
    for process in processes:
        process.start()

    # รอให้ process ทั้งหมดทำงานเสร็จสิ้น
    for process in processes:
        process.join()

    stability_ai.run_stability_ai()
    yolo_predictions.run_yolo_predictions()

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    main()
