# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reviewgANmgH.ui'
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

class Ui_ReviewWindow(object):
    def setupUi(self, ReviewWindow):
        if not ReviewWindow.objectName():
            ReviewWindow.setObjectName(u"ReviewWindow")
        ReviewWindow.resize(340, 384)
        self.gridLayout_2 = QGridLayout(ReviewWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.titleLabel = QLabel(ReviewWindow)
        self.titleLabel.setObjectName(u"titleLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.titleLabel)

        self.titleEdit = QLineEdit(ReviewWindow)
        self.titleEdit.setObjectName(u"titleEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.titleEdit)

        self.authorLabel = QLabel(ReviewWindow)
        self.authorLabel.setObjectName(u"authorLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.authorLabel)

        self.authorEdit = QLineEdit(ReviewWindow)
        self.authorEdit.setObjectName(u"authorEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.authorEdit)

        self.companyLabel = QLabel(ReviewWindow)
        self.companyLabel.setObjectName(u"companyLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.companyLabel)

        self.companyEdit = QLineEdit(ReviewWindow)
        self.companyEdit.setObjectName(u"companyEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.companyEdit)

        self.sourceLabel = QLabel(ReviewWindow)
        self.sourceLabel.setObjectName(u"sourceLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.sourceLabel)

        self.sourceEdit = QLineEdit(ReviewWindow)
        self.sourceEdit.setObjectName(u"sourceEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.sourceEdit)

        self.linkLabel = QLabel(ReviewWindow)
        self.linkLabel.setObjectName(u"linkLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.linkLabel)

        self.linkEdit = QLineEdit(ReviewWindow)
        self.linkEdit.setObjectName(u"linkEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.linkEdit)

        self.contentLabel = QLabel(ReviewWindow)
        self.contentLabel.setObjectName(u"contentLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.contentLabel)

        self.textEdit = QTextEdit(ReviewWindow)
        self.textEdit.setObjectName(u"textEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.textEdit)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ReviewWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(ReviewWindow)
        self.buttonBox.accepted.connect(ReviewWindow.accept)
        self.buttonBox.rejected.connect(ReviewWindow.reject)

        QMetaObject.connectSlotsByName(ReviewWindow)
    # setupUi

    def retranslateUi(self, ReviewWindow):
        ReviewWindow.setWindowTitle(QCoreApplication.translate("ReviewWindow", u"Dialog", None))
        self.titleLabel.setText(QCoreApplication.translate("ReviewWindow", u"T\u00edtulo:", None))
        self.authorLabel.setText(QCoreApplication.translate("ReviewWindow", u"Autor:", None))
        self.companyLabel.setText(QCoreApplication.translate("ReviewWindow", u"Empresa:", None))
        self.sourceLabel.setText(QCoreApplication.translate("ReviewWindow", u"Fonte:", None))
        self.linkLabel.setText(QCoreApplication.translate("ReviewWindow", u"Link:", None))
        self.contentLabel.setText(QCoreApplication.translate("ReviewWindow", u"Conte\u00fado:", None))
    # retranslateUi

