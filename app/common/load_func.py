# coding=utf-8
import os
import cv2
import numpy as np
from PIL import Image

# 获取人脸及对应标签函数
def seek_faces_ids_names(dataset_path):
    # 存储人脸、ID、姓名与路径
    temp_faces = []
    temp_ids = []
    temp_names = []
    image_paths = [os.path.join(dataset_path, file_name) for file_name in os.listdir(dataset_path)]

    # 检测器设置
    face_detector = cv2.CascadeClassifier('app/common/classifier/haarcascade_frontalface_default.xml')

    # 遍历图片并处理
    for single_image_path in image_paths:

        # 将图像灰度化并转化为numpy数组格式
        img_PIL = Image.open(single_image_path).convert('L')
        img_numpy = np.array(img_PIL, dtype='uint8')

        # 图像检测与数据存储
        face_position = face_detector.detectMultiScale(img_numpy)
        single_id = int(os.path.split(single_image_path)[1].split('_')[0])
        single_name = str(os.path.split(single_image_path)[1].split('_')[1].split('.')[0])
        for x, y, w, h in face_position:
            single_face = img_numpy[y:y+h, x:x+w]
            temp_ids.append(single_id)
            temp_faces.append(single_face)
            temp_names.append(single_name)

    return temp_faces, temp_ids, temp_names

# 路径参数
dataset_path  = 'app/common/images/'
try:
    # 获取人脸特征
    faces, ids, names = seek_faces_ids_names(dataset_path)

    # 模型加载并训练
    model = cv2.face.LBPHFaceRecognizer.create()
    model.train(faces, np.array(ids))

    # 模型与姓名信息保存
    if os.path.exists('app/common/features/harr.yml'):
        os.remove('app/common/features/harr.yml')
    model.write('app/common/features/harr.yml')
    name_file_path = 'app/common/features/name.txt'
    if os.path.exists(name_file_path):
        os.remove(name_file_path)
    with open(name_file_path, 'w') as name_file:
        for i in range(len(names)):
            name_file.write(names[i] + '\n')
except:
    from PyQt5.QtWidgets import QApplication, QMessageBox
    import sys
    app = QApplication(sys.argv)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("发生异常，请联系管理员处理")
    msg.setWindowTitle("错误")
    msg.exec_()