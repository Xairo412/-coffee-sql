import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.load_data()

    def load_data(self):
        data = self.con.execute("SELECT * FROM coffee").fetchall()
        column_names = [description[0] for description in self.con.execute("SELECT * FROM coffee").description]
        self.coffeWidget.setRowCount(len(data))
        self.coffeWidget.setColumnCount(len(column_names))
        self.coffeWidget.setHorizontalHeaderLabels(column_names)
        for row_index, row_data in enumerate(data):
            for column_index, item in enumerate(row_data):
                self.coffeWidget.setItem(row_index, column_index, QTableWidgetItem(str(item)))
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
