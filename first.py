import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPointF
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main1.ui', self)
        self.pushButton.clicked.connect(self.paintEvent)

    def paintEvent(self):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        self.update()
        qp.end()

    def draw(self, qp):
        s = random.randint(4, 50)
        qp.setBrush(QColor(245, 224, 66))
        qp.drawEllipse(self.x, self.y, s, s)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())