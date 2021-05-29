# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zipconverter_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 590)
        MainWindow.setMinimumSize(QtCore.QSize(500, 590))
        MainWindow.setMaximumSize(QtCore.QSize(500, 590))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        MainWindow.setFont(font)
        directory = os.path.dirname(os.path.realpath(__file__))
        parent_directory = os.path.split(directory)[0] + '/images'
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{parent_directory}/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(0, 0, 541, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("background-color: rgb(115, 115, 115);\n"
"color: rgb(242, 242, 242);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 501, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 15, 10, 15)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_select = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_select.sizePolicy().hasHeightForWidth())
        self.button_select.setSizePolicy(sizePolicy)
        self.button_select.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_select.setFont(font)
        self.button_select.setStyleSheet("background-color: rgb(166, 166, 166);\n"
"color: rgb(64, 64, 64);\n"
"border-color: rgb(115, 115, 115);\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-style: solid;")
        self.button_select.setObjectName("button_select")
        self.verticalLayout.addWidget(self.button_select)
        self.list_view = QtWidgets.QListWidget(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.list_view.setFont(font)
        self.list_view.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(64, 64, 64);\n"
"border-color: rgb(115, 115, 115);\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"padding: 5px;")
        self.list_view.setObjectName("list_view")
        self.verticalLayout.addWidget(self.list_view)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.check_box = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.check_box.setFont(font)
        self.check_box.setStyleSheet("color: rgb(64, 64, 64);\n"
"")
        self.check_box.setObjectName("check_box")
        self.horizontalLayout.addWidget(self.check_box)
        self.edit_pass = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.edit_pass.setFont(font)
        self.edit_pass.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(64, 64, 64);\n"
"border-color: rgb(115, 115, 115);\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"padding-left: 5px;")
        self.edit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_pass.setObjectName("edit_pass")
        self.horizontalLayout.addWidget(self.edit_pass)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.button_converter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_converter.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_converter.setFont(font)
        self.button_converter.setStyleSheet("background-color: rgb(166, 166, 166);\n"
"color: rgb(64, 64, 64);\n"
"border-color: rgb(115, 115, 115);\n"
"border-radius: 10px;\n"
"border-width: 2px;\n"
"border-style: solid;")
        self.button_converter.setObjectName("button_converter")
        self.verticalLayout.addWidget(self.button_converter)
        self.progress_bar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.verticalLayout.addWidget(self.progress_bar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Zip Compactor"))
        self.button_select.setText(_translate("MainWindow", "Select Files"))
        self.check_box.setText(_translate("MainWindow", "Password:"))
        self.button_converter.setText(_translate("MainWindow", "Compact"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())