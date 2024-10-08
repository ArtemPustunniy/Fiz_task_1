# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Results.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Results(object):
    def setupUi(self, Results):
        Results.setObjectName("Results")
        Results.resize(800, 600)

        self.background = QtWidgets.QLabel(Results)
        self.background.setGeometry(0, 0, 800, 600)  # Задаем размер на всю форму
        self.background.setPixmap(

            QtGui.QPixmap("error_photo.jpg").scaled(800, 600, QtCore.Qt.KeepAspectRatioByExpanding,
                                                    QtCore.Qt.SmoothTransformation))
        self.background.setObjectName("background")
        self.overlay = QtWidgets.QLabel(Results)
        self.overlay.setGeometry(0, 0, 800, 600)
        self.overlay.setStyleSheet("background-color: rgba(230, 230, 230, 230);")  # Черный полупрозрачный слой
        self.overlay.setObjectName("overlay")

        self.centralwidget = QtWidgets.QWidget(Results)
        self.centralwidget.setObjectName("centralwidget")
        self.Top_label = QtWidgets.QLabel(self.centralwidget)
        self.Top_label.setGeometry(QtCore.QRect(240, 10, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Top_label.setFont(font)
        self.Top_label.setObjectName("Top_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.base_2 = QtWidgets.QLabel(self.centralwidget)
        self.base_2.setGeometry(QtCore.QRect(20, 160, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.base_2.setFont(font)
        self.base_2.setObjectName("base_2")
        self.base_1 = QtWidgets.QLabel(self.centralwidget)
        self.base_1.setGeometry(QtCore.QRect(20, 110, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.base_1.setFont(font)
        self.base_1.setObjectName("base_1")
        self.base_3 = QtWidgets.QLabel(self.centralwidget)
        self.base_3.setGeometry(QtCore.QRect(20, 210, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.base_3.setFont(font)
        self.base_3.setObjectName("base_3")
        self.Base_1_cord = QtWidgets.QLabel(self.centralwidget)
        self.Base_1_cord.setGeometry(QtCore.QRect(50, 120, 201, 31))
        self.Base_1_cord.setText("")
        self.Base_1_cord.setObjectName("Base_1_cord")
        self.Base_2_cord = QtWidgets.QLabel(self.centralwidget)
        self.Base_2_cord.setGeometry(QtCore.QRect(50, 160, 201, 31))
        self.Base_2_cord.setText("")
        self.Base_2_cord.setObjectName("Base_2_cord")
        self.Base_3_cord = QtWidgets.QLabel(self.centralwidget)
        self.Base_3_cord.setGeometry(QtCore.QRect(50, 210, 201, 31))
        self.Base_3_cord.setText("")
        self.Base_3_cord.setObjectName("Base_3_cord")
        self.New_2 = QtWidgets.QLabel(self.centralwidget)
        self.New_2.setGeometry(QtCore.QRect(20, 370, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.New_2.setFont(font)
        self.New_2.setObjectName("New_2")
        self.New_3 = QtWidgets.QLabel(self.centralwidget)
        self.New_3.setGeometry(QtCore.QRect(20, 420, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.New_3.setFont(font)
        self.New_3.setObjectName("New_3")
        self.New_1_cord = QtWidgets.QLabel(self.centralwidget)
        self.New_1_cord.setGeometry(QtCore.QRect(50, 330, 201, 31))
        self.New_1_cord.setText("")
        self.New_1_cord.setObjectName("New_1_cord")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 280, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.New_2_cord = QtWidgets.QLabel(self.centralwidget)
        self.New_2_cord.setGeometry(QtCore.QRect(50, 370, 201, 31))
        self.New_2_cord.setText("")
        self.New_2_cord.setObjectName("New_2_cord")

        self.about_rad_1 = QtWidgets.QLabel(Results)
        self.about_rad_1.setGeometry(QtCore.QRect(260, 370, 190, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.about_rad_1.setFont(font)
        self.about_rad_1.setObjectName("about_rad_1")

        self.New_1 = QtWidgets.QLabel(self.centralwidget)
        self.New_1.setGeometry(QtCore.QRect(20, 320, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.New_1.setFont(font)
        self.New_1.setObjectName("New_1")
        self.New_3_cord = QtWidgets.QLabel(self.centralwidget)
        self.New_3_cord.setGeometry(QtCore.QRect(50, 420, 201, 31))
        self.New_3_cord.setText("")
        self.New_3_cord.setObjectName("New_3_cord")

        self.about_rad_2 = QtWidgets.QLabel(Results)
        self.about_rad_2.setGeometry(QtCore.QRect(260, 420, 190, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.about_rad_2.setFont(font)
        self.about_rad_2.setObjectName("about_rad_1")

        Results.setCentralWidget(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 500, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.menubar = QtWidgets.QMenuBar(Results)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Results.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Results)
        self.statusbar.setObjectName("statusbar")
        Results.setStatusBar(self.statusbar)

        self.retranslateUi(Results)
        QtCore.QMetaObject.connectSlotsByName(Results)

    def retranslateUi(self, Results):
        _translate = QtCore.QCoreApplication.translate
        Results.setWindowTitle(_translate("Results", "MainWindow"))
        self.Top_label.setText(_translate("Results", "Получившийся результат"))
        self.label.setText(_translate("Results", "Исходные координаты:"))
        self.label_2.setText(_translate("Results", "Новые координаты:"))
        self.pushButton.setText(_translate("Results", "Вернуться на главную"))
        # self.about_rad_1.setText(_translate("Results", "в радианах"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Results()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
