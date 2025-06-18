import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600,300,600,600) 
        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()
    

    def initUI(self):
        self.checkbox.setGeometry(30,0,500,100)
        self.checkbox.setStyleSheet("font-size: 30px;")

        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    
    def checkbox_changed(self, state):
        #state is a value 0 = unchecked, 1 = partially checked, 2= checked

        if state == Qt.Checked:
            print("You like food")
        else:
            print("You don't like food")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ =="__main__":
    main()