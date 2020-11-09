import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter, QColor
import random


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.is_draw = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.is_draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.is_draw:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        num = random.randint(1, 150)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(QPointF(250, 150), num, num)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec())
