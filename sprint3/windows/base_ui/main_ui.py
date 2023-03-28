# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainClerBh.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(220, 270)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainLayout = QGridLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.reviewBox = QGroupBox(self.centralwidget)
        self.reviewBox.setObjectName(u"reviewBox")
        self.horizontalLayout_3 = QHBoxLayout(self.reviewBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.reviewLayout = QVBoxLayout()
        self.reviewLayout.setObjectName(u"reviewLayout")
        self.reviewCreateButton = QPushButton(self.reviewBox)
        self.reviewCreateButton.setObjectName(u"reviewCreateButton")

        self.reviewLayout.addWidget(self.reviewCreateButton)

        self.reviewEditButton = QPushButton(self.reviewBox)
        self.reviewEditButton.setObjectName(u"reviewEditButton")

        self.reviewLayout.addWidget(self.reviewEditButton)

        self.reviewDeleteButton = QPushButton(self.reviewBox)
        self.reviewDeleteButton.setObjectName(u"reviewDeleteButton")

        self.reviewLayout.addWidget(self.reviewDeleteButton)


        self.horizontalLayout_3.addLayout(self.reviewLayout)


        self.mainLayout.addWidget(self.reviewBox, 1, 0, 1, 1)

        self.textBox = QGroupBox(self.centralwidget)
        self.textBox.setObjectName(u"textBox")
        self.horizontalLayout = QHBoxLayout(self.textBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textLayout = QVBoxLayout()
        self.textLayout.setObjectName(u"textLayout")
        self.textCreateButton = QPushButton(self.textBox)
        self.textCreateButton.setObjectName(u"textCreateButton")

        self.textLayout.addWidget(self.textCreateButton)

        self.textEditButton = QPushButton(self.textBox)
        self.textEditButton.setObjectName(u"textEditButton")

        self.textLayout.addWidget(self.textEditButton)

        self.textDeleteButton = QPushButton(self.textBox)
        self.textDeleteButton.setObjectName(u"textDeleteButton")

        self.textLayout.addWidget(self.textDeleteButton)


        self.horizontalLayout.addLayout(self.textLayout)


        self.mainLayout.addWidget(self.textBox, 0, 0, 1, 1)

        self.videoBox = QGroupBox(self.centralwidget)
        self.videoBox.setObjectName(u"videoBox")
        self.horizontalLayout_2 = QHBoxLayout(self.videoBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.videoLayout = QVBoxLayout()
        self.videoLayout.setObjectName(u"videoLayout")
        self.videoCreateButton = QPushButton(self.videoBox)
        self.videoCreateButton.setObjectName(u"videoCreateButton")

        self.videoLayout.addWidget(self.videoCreateButton)

        self.videoEditButton = QPushButton(self.videoBox)
        self.videoEditButton.setObjectName(u"videoEditButton")

        self.videoLayout.addWidget(self.videoEditButton)

        self.videoDeleteButton = QPushButton(self.videoBox)
        self.videoDeleteButton.setObjectName(u"videoDeleteButton")

        self.videoLayout.addWidget(self.videoDeleteButton)


        self.horizontalLayout_2.addLayout(self.videoLayout)


        self.mainLayout.addWidget(self.videoBox, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.mainLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.mainLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"IpoHub", None))
        self.reviewBox.setTitle(QCoreApplication.translate("MainWindow", u"An\u00e1lises", None))
        self.reviewCreateButton.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.reviewEditButton.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.reviewDeleteButton.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.textBox.setTitle(QCoreApplication.translate("MainWindow", u"Textos", None))
        self.textCreateButton.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.textEditButton.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.textDeleteButton.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.videoBox.setTitle(QCoreApplication.translate("MainWindow", u"Videos", None))
        self.videoCreateButton.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.videoEditButton.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.videoDeleteButton.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
    # retranslateUi

