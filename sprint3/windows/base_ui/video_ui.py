# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'videonfoerW.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_VideoWindow(object):
    def setupUi(self, VideoWindow):
        if not VideoWindow.objectName():
            VideoWindow.setObjectName(u"VideoWindow")
        VideoWindow.resize(350, 158)
        self.gridLayout_2 = QGridLayout(VideoWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(VideoWindow)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(VideoWindow)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(VideoWindow)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(VideoWindow)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_3 = QLabel(VideoWindow)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_3 = QLineEdit(VideoWindow)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(VideoWindow)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_4)

        self.label_4 = QLabel(VideoWindow)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(VideoWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(VideoWindow)
        self.buttonBox.accepted.connect(VideoWindow.accept)
        self.buttonBox.rejected.connect(VideoWindow.reject)

        QMetaObject.connectSlotsByName(VideoWindow)
    # setupUi

    def retranslateUi(self, VideoWindow):
        VideoWindow.setWindowTitle(QCoreApplication.translate("VideoWindow", u"VideoWindow", None))
        self.label.setText(QCoreApplication.translate("VideoWindow", u"T\u00edtulo:", None))
        self.label_2.setText(QCoreApplication.translate("VideoWindow", u"Autor:", None))
        self.label_3.setText(QCoreApplication.translate("VideoWindow", u"Fonte:", None))
        self.label_4.setText(QCoreApplication.translate("VideoWindow", u"Link:", None))
    # retranslateUi

