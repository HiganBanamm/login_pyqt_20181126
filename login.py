#导入两个ui界面.py文件
from Ui_hello import *
from Ui_login import login_MainWindow

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QMessageBox
from tkinter import messagebox


class my_hello(QMainWindow,hello_MainWindow):
    def __init__(self,parent=None):
        super(my_hello,self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        
class my_login(QMainWindow,login_MainWindow):
    def __init__(self,parent=None):
        super(my_login,self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        #绑定“确定事件按钮”
        self.pushButton.clicked.connect(self.judge)
        print('a')
        
    def judge(self):
        user_name = self.lineEdit.text() #获取用户名
        user_password = self.lineEdit_2.text() #获取密码
        print(user_name,user_password)
        
        #如果用户名和密码分别是admin和123456，
        #判断密码帐号是否正确，正确就会打开hello窗口，并且关闭登录框，如果不对，则会弹出警告框。
        if user_name =='admin' and user_password == '123456':
            
            hello_ui.show()
            ui.close()  
        else:
            QMessageBox.critical(self,'警告', '用户名或者密码错误')
        
    
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     ui = my_login()
     hello_ui = my_hello()
     ui.show()
     sys.exit(app.exec_())
    
