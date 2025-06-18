import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI")
        
        #(x, y, width, height)
        self.setGeometry(600,300,600,600) 

        #to set window icon
        #self.setWindowIcon(QIcon("/pic path here"))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    #by default window is hidden
    window.show()

    #Handles events
    sys.exit(app.exec_())

if __name__ =="__main__":
    main()