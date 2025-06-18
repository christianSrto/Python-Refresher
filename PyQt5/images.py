import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600,300,600,600) 

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("PyQt5/download.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)

        #to center image
        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) //2,
                          label.width(),
                          label.height())


        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ =="__main__":
    main()