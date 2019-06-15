import os
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton,QFileDialog,QApplication,QWidget
from kMainWidget import kMianWiget
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = kMianWiget()
    # btn = QPushButton("button",widget)
    widget.setMinimumSize(QSize(600,400))
    print("hello world")
    widget.show()
    sys.exit(app.exec()) 