# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'videoeQzbwZ.ui'
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
        VideoWindow.resize(350, 214)
        self.gridLayout_2 = QGridLayout(VideoWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.titleLabel = QLabel(VideoWindow)
        self.titleLabel.setObjectName(u"titleLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.titleLabel)

        self.titleEdit = QLineEdit(VideoWindow)
        self.titleEdit.setObjectName(u"titleEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.titleEdit)

        self.authorLabel = QLabel(VideoWindow)
        self.authorLabel.setObjectName(u"authorLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.authorLabel)

        self.authorEdit = QLineEdit(VideoWindow)
        self.authorEdit.setObjectName(u"authorEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.authorEdit)

        self.sourceLabel = QLabel(VideoWindow)
        self.sourceLabel.setObjectName(u"sourceLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.sourceLabel)

        self.sourceEdit = QLineEdit(VideoWindow)
        self.sourceEdit.setObjectName(u"sourceEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.sourceEdit)

        self.linkLabel = QLabel(VideoWindow)
        self.linkLabel.setObjectName(u"linkLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.linkLabel)

        self.linkEdit = QLineEdit(VideoWindow)
        self.linkEdit.setObjectName(u"linkEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.linkEdit)

        self.idLabel = QLabel(VideoWindow)
        self.idLabel.setObjectName(u"idLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.idLabel)

        self.idEdit = QLineEdit(VideoWindow)
        self.idEdit.setObjectName(u"idEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.idEdit)

        self.thumbnailLabel = QLabel(VideoWindow)
        self.thumbnailLabel.setObjectName(u"thumbnailLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.thumbnailLabel)

        self.thumbnailEdit = QLineEdit(VideoWindow)
        self.thumbnailEdit.setObjectName(u"thumbnailEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.thumbnailEdit)


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
        self.titleLabel.setText(QCoreApplication.translate("VideoWindow", u"T\u00edtulo:", None))
        self.authorLabel.setText(QCoreApplication.translate("VideoWindow", u"Autor:", None))
        self.sourceLabel.setText(QCoreApplication.translate("VideoWindow", u"Fonte:", None))
        self.linkLabel.setText(QCoreApplication.translate("VideoWindow", u"Link:", None))
        self.idLabel.setText(QCoreApplication.translate("VideoWindow", u"Video ID", None))
        self.thumbnailLabel.setText(QCoreApplication.translate("VideoWindow", u"Thumbnail", None))
    # retranslateUi

