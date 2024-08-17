# นำเข้าไฟล์ทั้งหมด
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

def run_flask_app(app, init_func, secret, token, port):
    init_func(secret, token)  # เรียก init เพื่อกำหนดค่า line_bot_api และ handler
    app.run(port=port)

def main():
    processes = []  # สร้าง list สำหรับเก็บ process

    processes.append(Process(target=run_flask_app, args=(PYLB001.app, PYLB001.init, channel_secret, channel_access_token, 5001)))
    processes.append(Process(target=run_flask_app, args=(PYLB002.app, PYLB002.init, channel_secret, channel_access_token, 5002)))
    processes.append(Process(target=run_flask_app, args=(PYLB003.app, PYLB003.init, channel_secret, channel_access_token, 5003)))
    processes.append(Process(target=run_flask_app, args=(PYLB004.app, PYLB004.init, channel_secret, channel_access_token, 5004)))
    processes.append(Process(target=run_flask_app, args=(PYLB005.app, PYLB005.init, channel_secret, channel_access_token, 5005)))
    processes.append(Process(target=run_flask_app, args=(PYLB006.app, PYLB006.init, channel_secret, channel_access_token, 5006)))
    processes.append(Process(target=run_flask_app, args=(PYLB007.app, PYLB007.init, channel_secret, channel_access_token, 5007)))
    processes.append(Process(target=run_flask_app, args=(PYLB008.app, PYLB008.init, channel_secret, channel_access_token, 5008)))
    processes.append(Process(target=run_flask_app, args=(PYLB009.app, PYLB009.init, channel_secret, channel_access_token, 5009)))
    processes.append(Process(target=run_flask_app, args=(PYLB010.app, PYLB010.init, channel_secret, channel_access_token, 5010)))
    processes.append(Process(target=run_flask_app, args=(PYLB011.init, channel_secret, channel_access_token, 5011)))
    processes.append(Process(target=run_flask_app, args=(PYLB012.app, PYLB012.init, channel_secret, channel_access_token, 5012)))
    processes.append(Process(target=run_flask_app, args=(PYLB013.app, PYLB013.init, channel_secret, channel_access_token, 5013)))
    processes.append(Process(target=run_flask_app, args=(PYLB014.app, PYLB014.init, channel_secret, channel_access_token, 5014)))
    processes.append(Process(target=run_flask_app, args=(PYLB015.app, PYLB015.init, channel_secret, channel_access_token, 5015)))
    # processes.append(Process(target=run_flask_app, args=(PYLB016.app, PYLB016.init, channel_secret, channel_access_token, 5016)))
    processes.append(Process(target=run_flask_app, args=(PYLB017.app, PYLB017.init, channel_secret, channel_access_token, 5017)))
    processes.append(Process(target=run_flask_app, args=(PYLB018.app, PYLB018.init, channel_secret, channel_access_token, 5018)))
    # processes.append(Process(target=run_flask_app, args=(PYLB019.app, PYLB019.init, channel_secret, channel_access_token, 5019)))
    # processes.append(Process(target=run_flask_app, args=(PYLB020.app, PYLB020.init, channel_secret, channel_access_token, 5020)))
    processes.append(Process(target=run_flask_app, args=(PYLB021.app, PYLB021.init, channel_secret, channel_access_token, 5021)))
    processes.append(Process(target=run_flask_app, args=(PYLB022.app, PYLB022.init, channel_secret, channel_access_token, 5022)))
    processes.append(Process(target=run_flask_app, args=(PYLB023.app, PYLB023.init, channel_secret, channel_access_token, 5023)))
    processes.append(Process(target=run_flask_app, args=(PYLB024.app, PYLB024.init, channel_secret, channel_access_token, 5024)))
    processes.append(Process(target=run_flask_app, args=(PYLB025.app, PYLB025.init, channel_secret, channel_access_token, 5025)))
    processes.append(Process(target=run_flask_app, args=(PYLB026.app, PYLB026.init, channel_secret, channel_access_token, 5026)))
    processes.append(Process(target=run_flask_app, args=(PYLB027.app, PYLB027.init, channel_secret, channel_access_token, 5027)))
    processes.append(Process(target=run_flask_app, args=(PYLB028.app, PYLB028.init, channel_secret, channel_access_token, 5028)))
    processes.append(Process(target=run_flask_app, args=(PYLB029.app, PYLB029.init, channel_secret, channel_access_token, 5029)))
    processes.append(Process(target=run_flask_app, args=(PYLB030.app, PYLB030.init, channel_secret, channel_access_token, 5030)))
    processes.append(Process(target=run_flask_app, args=(PYLB031.app, PYLB031.init, channel_secret, channel_access_token, 5031)))
    processes.append(Process(target=run_flask_app, args=(PYLB032.app, PYLB032.init, channel_secret, channel_access_token, 5032)))
    processes.append(Process(target=run_flask_app, args=(PYLB033.app, PYLB033.init, channel_secret, channel_access_token, 5033)))
    processes.append(Process(target=run_flask_app, args=(PYLB034.app, PYLB034.init, channel_secret, channel_access_token, 5034)))
    processes.append(Process(target=run_flask_app, args=(PYLB035.app, PYLB035.init, channel_secret, channel_access_token, 5035)))
    processes.append(Process(target=run_flask_app, args=(PYLB036.app, PYLB036.init, channel_secret, channel_access_token, 5036)))
    processes.append(Process(target=run_flask_app, args=(PYLB037.app, PYLB037.init, channel_secret, channel_access_token, 5037)))
    processes.append(Process(target=run_flask_app, args=(PYLB038.app, PYLB038.init, channel_secret, channel_access_token, 5038)))
    processes.append(Process(target=run_flask_app, args=(PYLB039.app, PYLB039.init, channel_secret, channel_access_token, 5039)))
    processes.append(Process(target=run_flask_app, args=(PYLB040.app, PYLB040.init, channel_secret, channel_access_token, 5040)))
    processes.append(Process(target=run_flask_app, args=(PYLB041.app, PYLB041.init, channel_secret, channel_access_token, 5041)))
    # processes.append(Process(target=run_flask_app, args=(PYLB042.app, PYLB042.init, channel_secret, channel_access_token, 5042)))
    processes.append(Process(target=run_flask_app, args=(PYLB043.app, PYLB043.init, channel_secret, channel_access_token, 5043)))
    processes.append(Process(target=run_flask_app, args=(PYLB044.app, PYLB044.init, channel_secret, channel_access_token, 5044)))
    # processes.append(Process(target=run_flask_app, args=(PYLB045.app, PYLB045.init, channel_secret, channel_access_token, 5045)))
    # processes.append(Process(target=run_flask_app, args=(PYLB046.app, PYLB046.init, channel_secret, channel_access_token, 5046)))
    processes.append(Process(target=run_flask_app, args=(PYLB047.app, PYLB047.init, channel_secret, channel_access_token, 5047)))
    processes.append(Process(target=run_flask_app, args=(PYLB048.app, PYLB048.init, channel_secret, channel_access_token, 5048)))
    # processes.append(Process(target=run_flask_app, args=(PYLB049.app, PYLB049.init, channel_secret, channel_access_token, 5049)))
    processes.append(Process(target=run_flask_app, args=(PYLB050.app, PYLB050.init, channel_secret, channel_access_token, 5050)))
    processes.append(Process(target=run_flask_app, args=(PYLB051.app, PYLB051.init, channel_secret, channel_access_token, 5051)))

    # เริ่มกระบวนการในแต่ละ process
    for process in processes:
        process.start()

    # รอให้ process ทั้งหมดทำงานเสร็จสิ้น
    for process in processes:
        process.join()

    stability_ai.run_stability_ai()
    yolo_predictions.run_yolo_predictions()

if __name__ == "__main__":
    main()
