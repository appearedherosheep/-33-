import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QDesktopWidget, QCalendarWidget
from PyQt5.QtCore import QDate
from main import call_ymd, return_breakfast, return_lunch, return_dinner, pretty_date, call_hmin


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('급식충곽33기')
        self.resize(350, 400)
        self.center()
        self.initUI()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        self.breakfast_btn = QPushButton('아침', self)
        self.lunch_btn = QPushButton('점심', self)
        self.dinner_btn = QPushButton('저녁', self)

        self.breakfast_btn.setCheckable(True)
        self.lunch_btn.setCheckable(True)
        self.dinner_btn.setCheckable(True)

        hbox = QHBoxLayout()
        hbox.addWidget(self.breakfast_btn)
        hbox.addWidget(self.lunch_btn)
        hbox.addWidget(self.dinner_btn)

        breakfast_list = return_breakfast(call_ymd())
        self.breakfast = QLabel(breakfast_list, self)
        self.breakfast.setFixedSize(350, 350)
        self.breakfast.setFont(QFont('나눔바른고딕', 20))
        self.breakfast.setStyleSheet(
            "color : black;"
            "border-style : Solid;"
            "border-width : 1px;"
            "border-color : #C9CED2;"
            "border-radius : 10px;"
            "background-color : white;"
        )

        lunch_list = return_lunch(call_ymd())
        self.lunch = QLabel(lunch_list, self)
        self.lunch.setFixedSize(350, 350)
        self.lunch.setFont(QFont('나눔바른고딕', 20))
        self.lunch.setStyleSheet(
            "color : black;"
            "border-style : Solid;"
            "border-width : 1px;"
            "border-color : #C9CED2;"
            "border-radius : 10px;"
            "background-color : white;"
        )

        dinner_list = return_dinner(call_ymd())
        self.dinner = QLabel(dinner_list, self)
        self.dinner.setFixedSize(350, 350)
        self.dinner.setFont(QFont('나눔바른고딕', 20))
        self.dinner.setStyleSheet(
            "color : black;"
            "border-style : Solid;"
            "border-width : 1px;"
            "border-color : #C9CED2;"
            "border-radius : 10px;"
            "background-color : white;"
        )

        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.setVerticalHeaderFormat(0)  # 옆에 주 표시 false

        self.cal.clicked[QDate].connect(self.change_menu)

        if call_hmin() >= 8 and call_hmin() < 13:
            self.show_lunch()
        else:
            self.show_dinner()

        if self.breakfast_btn.isChecked():
            self.show_breakfast()
        if self.lunch_btn.isChecked():
            self.show_lunch()
        if self.dinner_btn.isChecked():
            self.show_dinner()

        self.breakfast_btn.clicked.connect(self.show_breakfast)
        self.lunch_btn.clicked.connect(self.show_lunch)
        self.dinner_btn.clicked.connect(self.show_dinner)

        vbox = QVBoxLayout()
        vbox.addWidget(self.QLabel_date())
        vbox.addWidget(self.cal)
        vbox.addLayout(hbox)
        vbox.addWidget(self.breakfast)
        vbox.addWidget(self.lunch)
        vbox.addWidget(self.dinner)

        self.setLayout(vbox)

    def QLabel_date(self):
        self.date = QLabel(pretty_date())
        self.date.setFont(QFont('netmarble Medium', 17))
        return self.date

    def show_breakfast(self):
        self.lunch.hide()
        self.dinner.hide()
        self.breakfast.show()
        self.breakfast_btn.setChecked(True)
        self.lunch_btn.setChecked(False)
        self.dinner_btn.setChecked(False)

    def show_lunch(self):
        self.breakfast.hide()
        self.dinner.hide()
        self.lunch.show()
        self.breakfast_btn.setChecked(False)
        self.lunch_btn.setChecked(True)
        self.dinner_btn.setChecked(False)

    def show_dinner(self):
        self.breakfast.hide()
        self.lunch.hide()
        self.dinner.show()
        self.breakfast_btn.setChecked(False)
        self.lunch_btn.setChecked(False)
        self.dinner_btn.setChecked(True)

    def change_menu(self):
        date_cal = self.cal.selectedDate()
        date = date_cal.toString()
        yo1, mon, day, year = date.split()
        ymd = int(year)*10000+int(mon)*100+int(day)

        if yo1 == '토':
            self.breakfast.setText('오늘 토요일ㅎ')
            self.lunch.setText('오늘 토요일ㅎ')
            self.dinner.setText('오늘 토요일ㅎ')
        elif yo1 == '일':
            self.breakfast.setText('오늘 일요일ㅠ')
            self.lunch.setText('오늘 일요일ㅠ')
            self.dinner.setText('오늘 일요일ㅠ')
        else:
            self.breakfast.setText(return_breakfast(ymd))
            self.lunch.setText(return_lunch(ymd))
            self.dinner.setText(return_dinner(ymd))

            self.breakfast.repaint()
            self.lunch.repaint()
            self.dinner.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
