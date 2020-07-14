import sys
from PyQt5 import QtWidgets, QtCore
from UI.Ui_hoho import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.counter = QtCore.QTime()
        self.timer1 = QtCore.QTimer()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.setWindowTitle("計時器")
        self.timer1.timeout.connect(self.timer1_timeout)
        self.btstart.clicked.connect(self.btnStart_Click)
        self.show()

    def btnStart_Click(self):
        if self.btstart.text() == "開始計時":
            self.timer1.start(1)
            self.counter.restart()
            self.btstart.setText("停止")
        else:
            # print(self.counter.elapsed())
            self.btstart.setText("開始計時")
            self.timer1.stop()

    def timer1_timeout(self):
        totalms = self.counter.elapsed()
        self.lcdms.display(totalms % 1000)
        self.lcdsec.display((totalms // 1000) % 60)
        self.lcdmin.display(((totalms // 1000) // 60) % 60)
        self.lcdhr.display(((totalms // 1000) // 60) // 60)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWin = MyWindow()
    sys.exit(app.exec_())
