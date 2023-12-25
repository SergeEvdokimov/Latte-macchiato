import io
import sys
import sqlite3
import PyQt5.uic as uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractScrollArea
from variables import ui, add_edit_ui

con = sqlite3.connect("data\coffee.sqlite")
cur = con.cursor()


class AddEditCoffee(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        temp = io.StringIO(add_edit_ui)
        uic.loadUi(temp, self)

        self.closeButton.clicked.connect(self.close)
        self.statusbar = self.statusBar()

    def try_to_add(self):
        if self.get_adding_verdict():
            con.commit()
            self.parent().show_data()
            self.close()

    def get_adding_verdict(self):
        try:
            variety_name = self.variety_name.text()
            degree_of_roasting = self.degree_of_roasting.text()
            ground_or_in_grains = self.comboBox.currentText()
            taste_descr = self.taste_descr.text()
            price = int(self.price.text())
            volume_ml = int(self.volume_ml.text())

            if not variety_name or not degree_of_roasting or not taste_descr or price < 0 or volume_ml < 0:
                raise NameError

            cur.execute(f'''INSERT INTO coffee
            (variety_name, degree_of_roasting, ground_or_in_grains, taste_descr, price, volume_ml)
             VALUES("{variety_name}", "{degree_of_roasting}",
              "{ground_or_in_grains}", "{taste_descr}", {price}, {volume_ml})''')
            con.commit()
            return True

        except Exception:
            self.statusbar.showMessage('Неверно заполнена форма')
            return False

    def try_to_edit(self):
        if self.get_editing_verdict():
            con.commit()
            self.parent().show_data()
            self.close()

    def get_editing_verdict(self):
        try:
            variety_name = self.variety_name.text()
            degree_of_roasting = self.degree_of_roasting.text()
            ground_or_in_grains = self.comboBox.currentText()
            taste_descr = self.taste_descr.text()
            price = int(self.price.text())
            volume_ml = int(self.volume_ml.text())

            row = self.parent().tableWidget.currentRow()
            unic = int(self.parent().tableWidget.item(row, 0).text())

            if not variety_name or not degree_of_roasting or not taste_descr or price < 0 or volume_ml < 0:
                raise NameError

            cur.execute(f'''update coffee set
            variety_name = "{variety_name}", degree_of_roasting = "{degree_of_roasting}",
             ground_or_in_grains = "{ground_or_in_grains}", taste_descr = "{taste_descr}",
              price = {price}, volume_ml = {volume_ml} where id == {unic}''')
            con.commit()
            return True

        except Exception:
            self.statusbar.showMessage('Неверно заполнена форма')
            return False


class CoffeeHouse(QMainWindow):
    def __init__(self):
        super().__init__()

        temp = io.StringIO(ui)
        uic.loadUi(temp, self)
        self.setWindowTitle('Кофейня')
        self.show_data()
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.addButton.clicked.connect(self.add_coffee)
        self.editButton.clicked.connect(self.edit_coffee)
        self.status = self.statusBar()

    def show_data(self):
        query = cur.execute(f'''select * from coffee''').fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(len(query))
        title = ['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
                 'Описание вкуса', 'Цена,\nруб', 'Объем упаковки,\nмл']
        self.tableWidget.setHorizontalHeaderLabels(title)

        for i, elem in enumerate(query):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                self.tableWidget.item(i, j).setFlags(Qt.ItemIsDropEnabled | Qt.ItemIsSelectable)

        self.tableWidget.resizeColumnsToContents()

    def add_coffee(self):
        self.status.showMessage('')
        self.add_coffee_widget = AddEditCoffee(self)
        self.add_coffee_widget.show()
        self.add_coffee_widget.Button.clicked.connect(self.add_coffee_widget.try_to_add)

    def edit_coffee(self):
        self.status.showMessage('')
        self.edit_coffee_widget = AddEditCoffee(self)
        self.edit_coffee_widget.Button.clicked.connect(self.edit_coffee_widget.try_to_edit)

        row = self.tableWidget.currentRow()
        if row == -1:
            self.status.showMessage('Необходимо выбрать строчку')
        else:
            self.edit_coffee_widget.show()
            self.edit_coffee_widget.variety_name.setText(self.tableWidget.item(row, 1).text())
            self.edit_coffee_widget.degree_of_roasting.setText(self.tableWidget.item(row, 2).text())
            self.edit_coffee_widget.comboBox.setCurrentText(self.tableWidget.item(row, 3).text())
            self.edit_coffee_widget.taste_descr.setText(self.tableWidget.item(row, 4).text())
            self.edit_coffee_widget.price.setText(self.tableWidget.item(row, 5).text())
            self.edit_coffee_widget.volume_ml.setText(self.tableWidget.item(row, 6).text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoffeeHouse()
    window.show()
    sys.exit(app.exec())