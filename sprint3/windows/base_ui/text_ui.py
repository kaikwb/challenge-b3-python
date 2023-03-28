# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'textIrFSpj.ui'
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
    QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(340, 356)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.titleLabel = QLabel(Dialog)
        self.titleLabel.setObjectName(u"titleLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.titleLabel)

        self.titleEdit = QLineEdit(Dialog)
        self.titleEdit.setObjectName(u"titleEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.titleEdit)

        self.authorLabel = QLabel(Dialog)
        self.authorLabel.setObjectName(u"authorLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.authorLabel)

        self.authorEdit = QLineEdit(Dialog)
        self.authorEdit.setObjectName(u"authorEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.authorEdit)

        self.sourceLabel = QLabel(Dialog)
        self.sourceLabel.setObjectName(u"sourceLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.sourceLabel)

        self.sourceEdit = QLineEdit(Dialog)
        self.sourceEdit.setObjectName(u"sourceEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.sourceEdit)

        self.linkLabel = QLabel(Dialog)
        self.linkLabel.setObjectName(u"linkLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.linkLabel)

        self.linkEdit = QLineEdit(Dialog)
        self.linkEdit.setObjectName(u"linkEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.linkEdit)

        self.contentLabel = QLabel(Dialog)
        self.contentLabel.setObjectName(u"contentLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.contentLabel)

        self.contentEdit = QTextEdit(Dialog)
        self.contentEdit.setObjectName(u"contentEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.contentEdit)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"TextWindow", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"T\u00edtulo:", None))
        self.authorLabel.setText(QCoreApplication.translate("Dialog", u"Autor:", None))
        self.sourceLabel.setText(QCoreApplication.translate("Dialog", u"Fonte:", None))
        self.linkLabel.setText(QCoreApplication.translate("Dialog", u"Link:", None))
        self.contentLabel.setText(QCoreApplication.translate("Dialog", u"Conte\u00fado:", None))
    # retranslateUi

