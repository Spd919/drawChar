from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QSizePolicy
from PyQt5.QtChart import QChart, QChartView, QBarSet, \
    QBarSeries, QBarCategoryAxis,QValueAxis
import sys,os
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt



class BarChart(QWidget):
    def __init__(self,pred=[{'label':'S','prob':0.78}, {'label':'T', 'prob':0.1}, {'label':'U', 'prob':0.05}, {'label':'V','prob':0.03}, {'label':'W','prob':0.02}]):
        super().__init__()


        #window requirements
        self.setGeometry(200,200,560,560)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.setWindowTitle("Creating Barchart")
        self.setWindowIcon(QIcon("python.png"))

        #change the color of the window
        self.setStyleSheet('background-color:white')

        #create barseries
        set0 = QBarSet("Probability")


        #insert data to the barseries
        set0 << pred[0]['prob'] << pred[1]['prob'] << pred[2]['prob'] << pred[3]['prob'] << pred[4]['prob']

        #we want to create percent bar series
        series = QBarSeries()
        series.append(set0)

        #create chart and add the series in the chart
        chart = QChart()
        chart.addSeries(series)
        # chart.setTitleFont(QFont( "Helvetica", 32 ))
        # chart.setTitle("Predict result")
        chart.setAnimationOptions(QChart.SeriesAnimations)


        #create axis for the chart
        categories = [pred[0]['label'], pred[1]['label'], pred[2]['label'], pred[3]['label'], pred[4]['label']]

        axis = QBarCategoryAxis()
        axis.append(categories)

        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        axisY = QValueAxis()
        axisY.setRange(0, 1)
        axisY.setLabelFormat("%.2f")
        chart.setAxisY(axisY, series)


        chart.setTheme(QChart.ChartThemeHighContrast)
        chart.legend().setVisible(False)
        chart.setTitleFont(QFont('Arial',16 ))
        chart.setTitle("Predict result")
        #create chartview and add the chart in the chartview
        chartview = QChartView(chart)

        vbox = QVBoxLayout()
        vbox.addWidget(chartview)

        self.setLayout(vbox)







if __name__ == '__main__':
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    App = QApplication(sys.argv)
    window = BarChart()
    window.show()
    sys.exit(App.exec())