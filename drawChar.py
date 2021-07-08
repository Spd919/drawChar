import sys,os
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtWidgets import QLabel,QPushButton,QMainWindow,QWidget,QVBoxLayout,QHBoxLayout,QApplication
from PyQt5.QtGui import QPixmap,QColor,QPainter,QIcon

class Canvas(QLabel):
    def __init__(self):
        super().__init__()
        pixmap = QPixmap(280,280)
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None
        self.pen_color = QColor('#000000')

    def mouseMoveEvent(self,e):
        if self.last_x is None:
            self.last_x = e.x()
            self.last_y = e.y()
            return

        painter = QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(20)
        painter.setPen(p)
        painter.drawLine(self.last_x,self.last_y,e.x(),e.y())
        self.last_x = e.x()
        self.last_y = e.y()

        painter.end()
        self.update()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    def imgSave(self):
#        print(type(self.pixmap()))
        self.pixmap().save('test1.PNG')

    def imgClear(self):
        self.pixmap().fill(Qt.white)
        self.update()

class SaveButton(QPushButton):
    def __init__(self):
#        super().__init__(QIcon('./imgs/saveicon-white.png'),' Save')
        super().__init__('Save')
        button_stylesheet = ''' QPushButton {
                            font-size: 24px;
                            margin-left: auto;
                            margin-right: auto;
                            margin-bottom: 0;
                            padding: 10px 12px;
                            border: 1px solid transparent;
                            border-radius: 5px;
                            color: #fff;
                            background-color: #007bff;
                            border-color: #007bff;
                            }
                            QPushButton:hover {
                            color: #fff;
                            background-color: #0069d9;
                            border-color: #0062cc;
                            }
                            '''
        self.setStyleSheet(button_stylesheet)

class ClearButton(QPushButton):
    def __init__(self):
        super().__init__('Clear')
        button_stylesheet = ''' QPushButton {
                            font-size: 24px;
                            margin-left: auto;
                            margin-right: auto;
                            margin-bottom: 0;
                            padding: 10px 12px;
                            border: 1px solid transparent;
                            border-radius: 5px;
                            color: #fff;
                            background-color: #007bff;
                            border-color: #007bff;
                            }
                            QPushButton:hover {
                            color: #fff;
                            background-color: #0069d9;
                            border-color: #0062cc;
                            }
                            '''
        self.setStyleSheet(button_stylesheet)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas()
        widget_container = QWidget()
        vlayout = QVBoxLayout()
        widget_container.setLayout(vlayout)
        vlayout.addWidget(self.canvas)

        save_button = SaveButton()
        save_button.clicked.connect(self.canvas.imgSave)
        clear_button = ClearButton()
        clear_button.clicked.connect(self.canvas.imgClear)

        hlayout = QHBoxLayout()
        hlayout.addWidget(save_button)
        hlayout.addWidget(clear_button)
        vlayout.addLayout(hlayout)

        self.setCentralWidget(widget_container)

if __name__ == '__main__':
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()