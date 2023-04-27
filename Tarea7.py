# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:50:54 2023

@author: olive
"""
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("text-fields.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(3.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 20, 250, 200))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(520, 20, 250, 200))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 40, 200, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.separar_p)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 130, 200, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.separar_p)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 260, 741, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['Palabras','Vocales'])
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tarea 7"))
        self.pushButton.setText(_translate("MainWindow", "Separar Palabras"))
        self.pushButton_2.setText(_translate("MainWindow", "Contar letras por palabras"))

    def separar_p(self):
        text = self.textEdit.toPlainText()
        self.textEdit_2.setPlainText(text)
        split_text = text.split()
        
        for i in range(len(split_text),self.tableWidget.rowCount()):
            self.tableWidget.removeRow(len(split_text))
        
        for i in range(len(split_text)):
            rowAct = self.tableWidget.rowCount()
            if (rowAct <= i):
                self.tableWidget.insertRow(rowAct)
                self.tableWidget.setItem(i, 0,QtWidgets.QTableWidgetItem(split_text[i]))
            else:
                self.tableWidget.setItem(i, 0,QtWidgets.QTableWidgetItem(split_text[i]))
            
            # contar letras por palabra
            count_l = len(split_text[i])
            self.tableWidget.setItem(i, 1,QtWidgets.QTableWidgetItem(str(count_l)))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())