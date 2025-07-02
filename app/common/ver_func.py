# coding=utf-8
import cv2
from PyQt5.QtWidgets import QApplication, QMessageBox

# 基本参数
max = 500

# 加载模型与姓名
model = cv2.face.LBPHFaceRecognizer_create()
model.read('app/common/features/harr.yml')
name_file = open('app/common/features/name.txt', 'r')
names = name_file.readlines()
name_file.close()

# 摄像头加载
try:
    cap_video = cv2.VideoCapture(0)
except:
    app = QApplication([])
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle("Error")
    msg_box.setText("摄像头存在问题，请检查后重新执行程序")
    msg_box.exec_()
    exit()

def face_recognize():
    while True:
        flag, img = cap_video.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_detector = cv2.CascadeClassifier('app/common/classifier/haarcascade_frontalface_default.xml')
        face = face_detector.detectMultiScale(gray, minSize=(150, 150))
        for x, y, w, h in face:
            cv2.rectangle(img, (x, y), (x + w, y + h), color=(183, 104, 0), thickness= 5)
            id, deconfidence = model.predict(gray[y:y+h, x:x+w])
            if deconfidence > 80:
                cv2.putText(img, 'Stranger', (x + 10, y - 10), cv2.FONT_ITALIC, 0.75, (0,0,255)
                            , 3)
            else:
                cv2.putText(img, 'User: ' + str(names[id - 1]).split('\n')[0], (x + 10, y - 100), cv2.FONT_ITALIC, 0.75,
                            (255,0,0),3)
        cv2.imshow("System Working(Press 'q' to quit)", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            cap_video.release()
            cv2.destroyAllWindows()
            exit()

face_recognize()




