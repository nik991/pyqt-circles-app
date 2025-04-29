import sys
import random
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.drawButton.clicked.connect(self.draw_circle)
        self.circles = []
        
    def draw_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter - 50)
        self.circles.append((x, y, diameter))
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.yellow)
        painter.setBrush(QColor(255, 255, 0))
        for x, y, diameter in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
