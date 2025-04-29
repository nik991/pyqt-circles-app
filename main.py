import sys
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QVBoxLayout, QPushButton)
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt

class CircleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('Random Color Circles')
        self.setGeometry(100, 100, 600, 400)
        
        # Central widget setup
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout and widgets
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Canvas for drawing
        self.canvas = QWidget()
        self.canvas.setStyleSheet("background-color: white;")
        layout.addWidget(self.canvas)
        
        # Button to add circles
        self.draw_btn = QPushButton("Add Random Circle")
        self.draw_btn.clicked.connect(self.add_circle)
        layout.addWidget(self.draw_btn)
    
    def add_circle(self):
        # Generate random circle parameters
        diameter = random.randint(20, 100)
        x = random.randint(0, self.canvas.width() - diameter)
        y = random.randint(0, self.canvas.height() - diameter)
        color = QColor(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        
        self.circles.append((x, y, diameter, color))
        self.canvas.update()
    
    def paintEvent(self, event):
        painter = QPainter(self.canvas)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        for x, y, diameter, color in self.circles:
            painter.setPen(color)
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)
        
        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleWindow()
    window.show()
    sys.exit(app.exec())
