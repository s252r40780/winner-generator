from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import *

app=QApplication([])
mw = QWidget()
mw.setWindowTitle('Определитель победителя')
mw.resize(400,200)
lb1 = QLabel('Нажми, чтобы узнать победителя')
lb2 = QLabel('?')
button = QPushButton('Сгенерировать')
line = QVBoxLayout()
mw.setLayout(line)
def show_win():
    num = randint(1,100)
    lb2.setText(str(num))
    lb1.setText("Победитель")

button.clicked.connect(show_win)

line.addWidget(lb1, alignment= Qt.AlignCenter)
line.addWidget(lb2, alignment= Qt.AlignCenter)
line.addWidget(button, alignment= Qt.AlignCenter)
mw.show()
app.exec()
