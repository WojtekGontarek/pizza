import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # self.ui.small.toggled.connect()
        # self.ui.normal.toggled.connect()
        # self.ui.big.toggled.connect()
        #
        # self.ui.salamiBox.toggled.connect()
        # self.ui.doublecheeseBox.toggled.connect()
        # self.ui.pineappleBox.toggled.connect()
        # self.ui.mushroomBox.toggled.connect()
        self.ui.orderButton.clicked.connect(self.calculate)
        self.show()

    def calculate(self):
        result = self.result()
        size = "none"
        dodatki = []
        if self.ui.small.isChecked():
            size = "small"
        elif self.ui.normal.isChecked():
            size = "normal"
        elif self.ui.big.isChecked():
            size = "big"

        if self.ui.salamiBox.isChecked():
            dodatki.append("salami")
        if self.ui.doublecheeseBox.isChecked():
            dodatki.append("doublecheese")
        if self.ui.pineappleBox.isChecked():
            dodatki.append("pineapple")
        if self.ui.mushroomBox.isChecked():
            dodatki.append("mushroom")

        output = size+'  ' + ", ".join(dodatki)
        self.ui.result.setText(output)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())