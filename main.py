#######################################################
##        Configuração do WBP ProServer             ##
#                   versão 1.0                       #
#               desenvolvido pela WBP                #
######################################################

######################################################
############     IMPORT INTERFACE ####################
import sys
from  interface import *
from PyQt5.QtWidgets import QMainWindow, QApplication

######################################################

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())