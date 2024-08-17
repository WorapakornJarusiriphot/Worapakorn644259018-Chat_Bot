# นำเข้าไฟล์ทั้งหมด
from multiprocessing import Process
from dotenv import load_dotenv # type: ignore
import os
from multiprocessing import Process
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

load_dotenv()

channel_secret = os.getenv("CHANNEL_SECRET")
channel_access_token = os.getenv("CHANNEL_ACCESS_TOKEN")

def run_flask_app(app, port):
    app.run(port=port)

def main():
    # เรียกใช้ฟังก์ชันหรือรันโค้ดจากไฟล์ต่าง ๆ ตามลำดับที่ต้องการ
    # รันแอปพลิเคชัน Flask จากไฟล์ที่นำเข้า
    process.append(Process(target=run_flask_app, args=(PYLB001.app, 5001)))
    process.append(Process(target=run_flask_app, args=(PYLB002.app, 5002)))
    process.append(Process(target=run_flask_app, args=(PYLB003.app, 5003)))
    process.append(Process(target=run_flask_app, args=(PYLB004.app, 5004)))
    process.append(Process(target=run_flask_app, args=(PYLB005.app, 5005)))
    process.append(Process(target=run_flask_app, args=(PYLB006.app, 5006)))
    process.append(Process(target=run_flask_app, args=(PYLB007.app, 5007)))
    process.append(Process(target=run_flask_app, args=(PYLB008.app, 5008)))
    process.append(Process(target=run_flask_app, args=(PYLB009.app, 5009)))
    process.append(Process(target=run_flask_app, args=(PYLB010.app, 5010)))
    process.append(Process(target=run_flask_app, args=(PYLB011.app, 5011)))
    process.append(Process(target=run_flask_app, args=(PYLB012.app, 5012)))
    process.append(Process(target=run_flask_app, args=(PYLB013.app, 5013)))
    process.append(Process(target=run_flask_app, args=(PYLB014.app, 5014)))
    process.append(Process(target=run_flask_app, args=(PYLB015.app, 5015)))
    process.append(Process(target=run_flask_app, args=(PYLB016.app, 5016)))
    process.append(Process(target=run_flask_app, args=(PYLB017.app, 5017)))
    process.append(Process(target=run_flask_app, args=(PYLB018.app, 5018)))
    process.append(Process(target=run_flask_app, args=(PYLB019.app, 5019)))
    process.append(Process(target=run_flask_app, args=(PYLB020.app, 5020)))
    process.append(Process(target=run_flask_app, args=(PYLB021.app, 5021)))
    process.append(Process(target=run_flask_app, args=(PYLB022.app, 5022)))
    process.append(Process(target=run_flask_app, args=(PYLB023.app, 5023)))
    process.append(Process(target=run_flask_app, args=(PYLB024.app, 5024)))
    process.append(Process(target=run_flask_app, args=(PYLB025.app, 5025)))
    process.append(Process(target=run_flask_app, args=(PYLB026.app, 5026)))
    process.append(Process(target=run_flask_app, args=(PYLB027.app, 5027)))
    process.append(Process(target=run_flask_app, args=(PYLB028.app, 5028)))
    process.append(Process(target=run_flask_app, args=(PYLB029.app, 5029)))
    process.append(Process(target=run_flask_app, args=(PYLB030.app, 5030)))
    process.append(Process(target=run_flask_app, args=(PYLB031.app, 5031)))
    process.append(Process(target=run_flask_app, args=(PYLB032.app, 5032)))
    process.append(Process(target=run_flask_app, args=(PYLB033.app, 5033)))
    process.append(Process(target=run_flask_app, args=(PYLB034.app, 5034)))
    process.append(Process(target=run_flask_app, args=(PYLB035.app, 5035)))
    process.append(Process(target=run_flask_app, args=(PYLB036.app, 5036)))
    process.append(Process(target=run_flask_app, args=(PYLB037.app, 5037)))
    process.append(Process(target=run_flask_app, args=(PYLB038.app, 5038)))
    process.append(Process(target=run_flask_app, args=(PYLB039.app, 5039)))
    process.append(Process(target=run_flask_app, args=(PYLB040.app, 5040)))
    process.append(Process(target=run_flask_app, args=(PYLB041.app, 5041)))
    process.append(Process(target=run_flask_app, args=(PYLB042.app, 5042)))
    process.append(Process(target=run_flask_app, args=(PYLB043.app, 5043)))
    process.append(Process(target=run_flask_app, args=(PYLB044.app, 5044)))
    process.append(Process(target=run_flask_app, args=(PYLB045.app, 5045)))
    process.append(Process(target=run_flask_app, args=(PYLB046.app, 5046)))
    process.append(Process(target=run_flask_app, args=(PYLB047.app, 5047)))
    process.append(Process(target=run_flask_app, args=(PYLB048.app, 5048)))
    process.append(Process(target=run_flask_app, args=(PYLB049.app, 5049)))
    process.append(Process(target=run_flask_app, args=(PYLB050.app, 5050)))
    process.append(Process(target=run_flask_app, args=(PYLB051.app, 5051)))
    # ...

    for process in process:
        process.start()

    for process in process:
        process.join()

    stability_ai.run_stability_ai()
    yolo_predictions.run_yolo_predictions()

if __name__ == "__main__":
    main()
