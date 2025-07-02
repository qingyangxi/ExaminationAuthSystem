# coding=utf-8
import cv2
from PyQt5.QtWidgets import QApplication, QMessageBox
import sys

# 基本参数
flag = 1
id = 1
max = 50000

# 导入摄像头
try:
    cap_video = cv2.VideoCapture(0)
except:
    app = QApplication(sys.argv)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("摄像头存在问题，请检查后重新执行程序")
    msg.setWindowTitle("错误")
    msg.exec_()
    exit()

# 姓名读取
name = []
for i in range(max):
    name.append(0)
from PyQt5.QtWidgets import QInputDialog

app = QApplication(sys.argv)
name[id], ok = QInputDialog.getText(None, "输入姓名", "请输入将要读取的对象的姓名：")
if not ok:
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("姓名输入被取消")
    msg.setWindowTitle("信息")
    msg.exec_()
    exit()

# 姓名检测
def name_detect():
    if name[id] == 0:
        name[id], ok = QInputDialog.getText(None, "输入姓名", "请输入新人的姓名：")
        if not ok:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("姓名输入被取消")
            msg.setWindowTitle("信息")
            msg.exec_()
            exit()

# 图片读取
while cap_video.isOpened():
    ret_value, video_input = cap_video.read()
    cv2.namedWindow(f"Now:{id}, Press S to Save, B to back, N to continue, Q to quit", cv2.WINDOW_NORMAL)
    cv2.resizeWindow(f"Now:{id}, Press S to Save, B to back, N to continue, Q to quit", 1000, 800)
    screen_width = cv2.getWindowImageRect(f"Now:{id}, Press S to Save, B to back, N to continue, Q to quit")[2]
    screen_height = cv2.getWindowImageRect(f"Now:{id}, Press S to Save, B to back, N to continue, Q to quit")[3]
    cv2.moveWindow(f"Now:{id}, Press S to Save, B to back, N to continue, Q to quit", (screen_width) // 2 + 300, (screen_height) // 2)
    cv2.imshow(f"Now:{id}, Press S to Save, B to back, N to continue, Q to quit", video_input)
    key = cv2.waitKey(1)
    if key == ord('s'):
        if cv2.imwrite("app/common/images/" + str(id) + "_" + str(name[id]) + ".jpg", video_input):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("当前对象图片采集成功")
            msg.setWindowTitle("信息")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("当前对象图片无法保存，请检查程序权限")
            msg.setWindowTitle("错误")
            msg.exec_()
    elif key == ord('n'):
        if id + 1 < max:
            id = id + 1
            cv2.destroyAllWindows()
            name_detect()
            continue
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("当前已达到可存储数据的上限，请联系管理员修改上限")
            msg.setWindowTitle("信息")
            msg.exec_()
    elif key == ord('b'):
        if id - 1 > 0:
            id = id - 1
            cv2.destroyAllWindows()
            name_detect()
            continue
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("已是第一个信息")
            msg.setWindowTitle("信息")
            msg.exec_()
    elif key == ord('q'):
        break
    else:
        continue

# 释放摄像头与内存
cap_video.release()
cv2.destroyAllWindows()