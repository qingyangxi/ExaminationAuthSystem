# 全国二次元招生全国统一考试身份识别系统——人脸识别系统大一年度项目程序案例

## 使用方法

创建虚拟环境

```py
python -m venv venv
```

激活虚拟环境 (Windows)

```sh
.\venv\Scripts\activate
```

安装所需的Python库

```py
pip install opencv-python
pip install opencv-contrib-python
pip install "PyQt-Fluent-Widgets[full]" -i https://pypi.org/simple/
```

运行程序
```sh
python main.py
```

## 已知问题

- 界面布局
- 使用一次后需删除app/common/features中的所有文件和app/common/images中的所有文件，否则会报错