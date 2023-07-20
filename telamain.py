import sys
from PySide2.QtWidgets import(QApplication, QMainWindow, QWidget)
from PySide2.QtWidgets import(QApplication, QFileDialog,
 QMainWindow, QMessageBox, QTreeWidgetItem, QWidget)
from ui_login import Ui_Login
from ui_main import Ui_MainWindow

class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        

        self.btn_login.clicked.connect(self.checkLogin)
        
    def checkLogin(self):

        if self.txt_password.text() =="123":
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            print("Senha inválida")

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gerenciamento")
      

        

        #*************PAGINAS DO SISTEMA***********************************************
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_tables.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_table))
        self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contato))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        self.btn_pg_cadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))
        self.btn_pg_import.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_import))

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()