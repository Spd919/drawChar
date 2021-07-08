import sys,os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow,QWidget,QVBoxLayout,QHBoxLayout,QApplication
from drawChar import Canvas,ClearButton,SaveButton
from chart_sample import BarChart



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas()
        self.canvas.setStyleSheet('border: 4px solid #C0C0C0;')
        widget_container = QWidget()
        self.setCentralWidget(widget_container)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.canvas)

        hlayout = QHBoxLayout()
        hlayout.addLayout(vlayout)
        barchart = BarChart()
        hlayout.addWidget(barchart)
        widget_container.setLayout(hlayout)

        save_button = SaveButton()
        save_button.clicked.connect(self.canvas.imgSave)
        clear_button = ClearButton()
        clear_button.clicked.connect(self.canvas.imgClear)

        hbuttonlayout = QHBoxLayout()
        hbuttonlayout.addWidget(save_button)
        hbuttonlayout.addWidget(clear_button)
        vlayout.addLayout(hbuttonlayout)

        self.setGeometry(50,50,700,200)
        self.setStyleSheet('background-color:white')






if __name__ == '__main__':
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()