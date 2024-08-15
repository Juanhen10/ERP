# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceKCiToI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
from PyQt5.QtWidgets import QMainWindow, QApplication


from Custom_Widgets.Widgets import QCustomSlideMenu
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(690, 508)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"    border: none;\n"
"	background-color: trasparent;\n"
"    color: #ffff;\n"
"}\n"
"#centralwidget{\n"
"     background-color: #00D877\n"
"}\n"
"\n"
"#slide_menu{\n"
"		background-color: #1E1E1E;\n"
"		border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding: 15px;\n"
"    background-color:  #00D877;\n"
"	border-radius: 5px\n"
"\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setFrameShape(QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.background_menu = QFrame(self.header)
        self.background_menu.setObjectName(u"background_menu")
        self.background_menu.setMinimumSize(QSize(0, 30))
        self.background_menu.setMaximumSize(QSize(16777215, 30))
        self.background_menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.background_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.menu_btn = QPushButton(self.background_menu)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setGeometry(QRect(10, 5, 81, 21))
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.background_menu, 0, Qt.AlignmentFlag.AlignLeft)

        self.background_title = QFrame(self.header)
        self.background_title.setObjectName(u"background_title")
        self.background_title.setFrameShape(QFrame.Shape.StyledPanel)
        self.background_title.setFrameShadow(QFrame.Shadow.Raised)
        self.title_txt = QLabel(self.background_title)
        self.title_txt.setObjectName(u"title_txt")
        self.title_txt.setGeometry(QRect(10, 10, 292, 31))
        self.title_txt.setMinimumSize(QSize(0, 5))
        self.title_txt.setMaximumSize(QSize(16777215, 16777206))
        font = QFont()
        font.setFamilies([u"Josefin Sans SemiBold"])
        font.setPointSize(12)
        font.setWeight(QFont.Black)
        font.setItalic(False)
        self.title_txt.setFont(font)
        self.title_txt.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.title_txt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.background_title)


        self.verticalLayout.addWidget(self.header)

        self.home = QFrame(self.centralwidget)
        self.home.setObjectName(u"home")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home.sizePolicy().hasHeightForWidth())
        self.home.setSizePolicy(sizePolicy)
        self.home.setStyleSheet(u"background-color: #00D877")
        self.home.setFrameShape(QFrame.Shape.StyledPanel)
        self.home.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.home)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.slide_menu = QCustomSlideMenu(self.home)
        self.slide_menu.setObjectName(u"slide_menu")
        self.slide_menu.setStyleSheet(u"\n"
"		background-color: #1E1E1E;\n"
"		border-radius: 20px;\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.slide_menu)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menus = QFrame(self.slide_menu)
        self.menus.setObjectName(u"menus")
        self.menus.setMinimumSize(QSize(150, 0))
        self.menus.setMaximumSize(QSize(150, 16777215))
        self.menus.setStyleSheet(u"QPushButton{\n"
"	padding: 15px;\n"
"    background-color:  #00D877;\n"
"	border-radius: 5px\n"
"\n"
"}")
        self.menus.setFrameShape(QFrame.Shape.StyledPanel)
        self.menus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menus)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.RH_btn = QPushButton(self.menus)
        self.RH_btn.setObjectName(u"RH_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/users.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.RH_btn.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.RH_btn)

        self.helpdesk_btn = QPushButton(self.menus)
        self.helpdesk_btn.setObjectName(u"helpdesk_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/monitor.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpdesk_btn.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.helpdesk_btn)

        self.capacitaPro_btn = QPushButton(self.menus)
        self.capacitaPro_btn.setObjectName(u"capacitaPro_btn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/codesandbox.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.capacitaPro_btn.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.capacitaPro_btn)

        self.finance_btn = QPushButton(self.menus)
        self.finance_btn.setObjectName(u"finance_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/dollar-sign.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.finance_btn.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.finance_btn)


        self.horizontalLayout_4.addWidget(self.menus, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout.addWidget(self.slide_menu)

        self.main_body = QFrame(self.home)
        self.main_body.setObjectName(u"main_body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy1)
        self.main_body.setStyleSheet(u"background-color: #1E1E1E;\n"
"border-radius: 10px")
        self.main_body.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.main_body)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.main_body)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setWeight(QFont.Light)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.main_body)


        self.verticalLayout.addWidget(self.home)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.title_txt.setText(QCoreApplication.translate("MainWindow", u"WBP ServePRO", None))
        self.RH_btn.setText(QCoreApplication.translate("MainWindow", u"RH", None))
        self.helpdesk_btn.setText(QCoreApplication.translate("MainWindow", u"WBP HelpDesk", None))
        self.capacitaPro_btn.setText(QCoreApplication.translate("MainWindow", u"CapacitaPro", None))
        self.finance_btn.setText(QCoreApplication.translate("MainWindow", u"Financeiro", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MAIN-BODY", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()  # Aqui está correto - chamando show() na instância de QMainWindow
    sys.exit(app.exec())