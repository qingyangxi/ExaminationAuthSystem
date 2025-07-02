# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem
from qfluentwidgets import CardWidget, HorizontalFlipView, IconWidget, LargeTitleLabel, PushButton, SubtitleLabel, TitleLabel, ImageLabel
from qfluentwidgets import ExpandLayout, ScrollArea  # Add this import
import sys
from qfluentwidgets import FluentIcon as FIF
from PyQt5.QtCore import Qt
from qfluentwidgets import BodyLabel, CaptionLabel, TransparentToolButton, FluentIcon
from PyQt5.QtCore import QSize
from ..common import resource
import os
import time

# QtCore.QCoreApplication.addLibraryPath(os.path.join(os.path.dirname(QtCore.__file__), "plugins"))

class AppCard(CardWidget):

    def __init__(self, icon, title, content, parent=None):
        super().__init__(parent)
        self.iconWidget = IconWidget(icon)
        self.titleLabel = BodyLabel(title, self)
        self.contentLabel = CaptionLabel(content, self)
        self.openButton = PushButton("进入", self)
        self.moreButton = TransparentToolButton(FluentIcon.MORE, self)

        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()

        self.setFixedHeight(73)
        self.setFixedWidth(830)
        self.iconWidget.setFixedSize(30, 30)
        self.contentLabel.setTextColor("#606060", "#d2d2d2")
        self.openButton.setFixedWidth(120)

        self.hBoxLayout.setContentsMargins(20, 11, 11, 11)
        self.hBoxLayout.setSpacing(15)
        self.hBoxLayout.addWidget(self.iconWidget)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.addWidget(self.contentLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.setAlignment(Qt.AlignVCenter)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.openButton, 0, Qt.AlignRight)
        self.hBoxLayout.addWidget(self.moreButton, 0, Qt.AlignRight)

        self.moreButton.setFixedSize(32, 32)


class FunctionInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, function):     
        function.setObjectName("function")
        function.resize(900, 700)
        
        # function.setWindowIcon(icon)
        self.SubtitleLabel = SubtitleLabel(function)
        self.SubtitleLabel.setGeometry(QtCore.QRect(40, 110, 511, 28))
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        subtitle_font = QtGui.QFont()
        subtitle_font.setFamily("微软雅黑")
        subtitle_font.setPointSize(15)
        self.SubtitleLabel.setFont(subtitle_font)

        self.LargeTitleLabel = LargeTitleLabel(function)
        self.LargeTitleLabel.setGeometry(QtCore.QRect(40, 40, 831, 54))
        self.LargeTitleLabel.setObjectName("LargeTitleLabel")
        large_title_font = QtGui.QFont()
        large_title_font.setFamily("微软雅黑")
        large_title_font.setPointSize(25)
        large_title_font.setBold(True)
        self.LargeTitleLabel.setFont(large_title_font)

        self.verCard = AppCard(FIF.SEARCH_MIRROR, "考生身份比对", "核验考生信息", self)
        self.verCard.openButton.clicked.connect(self.openVer)
        self.getCard = AppCard(FIF.ADD, "考生信息录入", "录入考生信息", self)
        self.getCard.openButton.clicked.connect(self.openGet)

        self.scrollWidget = QWidget()
        self.cardLayout = ExpandLayout(self.scrollWidget)
        self.cardLayout.setSpacing(20)
        self.cardLayout.setContentsMargins(40, 540, 0, 0)

        self.cardLayout.addWidget(self.verCard)
        self.cardLayout.addWidget(self.getCard)

        self.cardContainer = QWidget(function)
        self.cardContainer.setLayout(self.cardLayout)
        self.cardContainer.setObjectName("cardContainer")
        # self.cardContainer.setGeometry(QtCore.QRect(30, 540, 870, 200))

        self.imageLabel = ImageLabel(':/app/images/wallpaper.jpg', self) 
        self.imageLabel.resize(1200, 330)
        self.imageLabel.setObjectName("imageLabel")

        self.layout = QVBoxLayout(self)
        self.layout.addSpacing(10)
        self.layout.addWidget(self.LargeTitleLabel, 0, Qt.AlignTop)
        self.layout.addSpacing(8)
        self.layout.addWidget(self.SubtitleLabel, 0, Qt.AlignLeft)
        self.layout.addSpacing(10)
        self.layout.addWidget(self.imageLabel, 0, Qt.AlignCenter)
        self.layout.addSpacing(200)

        self.retranslateUi(function)
        QtCore.QMetaObject.connectSlotsByName(function)

    def retranslateUi(self, function):
        _translate = QtCore.QCoreApplication.translate
        function.setWindowTitle(_translate("function", "function"))
        self.SubtitleLabel.setText(_translate("function", "     Two Ci Yuan Examination Security System🎇"))
        self.LargeTitleLabel.setText(_translate("function", "   欢迎使用全国二次元统一考试身份验证系统👋"))
    
    def openVer(self):
        os.system("python app/common/ver_func.py")
    
    def openGet(self):
        os.system("python app/common/get_func.py")
        os.system("python app/common/load_func.py")
 
