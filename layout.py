# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(589, 315)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 571, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 4, 1, 1)
        self.normal = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.normal.setObjectName("normal")
        self.gridLayout.addWidget(self.normal, 0, 2, 1, 1)
        self.pineappleBox = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.pineappleBox.setCheckable(False)
        self.pineappleBox.setObjectName("pineappleBox")
        self.gridLayout.addWidget(self.pineappleBox, 4, 3, 1, 2)
        self.mushroomBox = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.mushroomBox.setObjectName("mushroomBox")
        self.gridLayout.addWidget(self.mushroomBox, 1, 3, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 4, 3)
        self.doublecheeseBox = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.doublecheeseBox.setObjectName("doublecheeseBox")
        self.gridLayout.addWidget(self.doublecheeseBox, 3, 3, 1, 2)
        self.big = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.big.setObjectName("big")
        self.gridLayout.addWidget(self.big, 0, 3, 1, 2)
        self.salamiBox = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.salamiBox.setObjectName("salamiBox")
        self.gridLayout.addWidget(self.salamiBox, 2, 3, 1, 2)
        self.result = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.result.setMaximumSize(QtCore.QSize(16777215, 80))
        self.result.setText("")
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 6, 0, 1, 5)
        self.orderButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.orderButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.orderButton.setObjectName("orderButton")
        self.gridLayout.addWidget(self.orderButton, 5, 1, 1, 3)
        self.small = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.small.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.small.setObjectName("small")
        self.gridLayout.addWidget(self.small, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.normal.setText(_translate("Dialog", "Pizza normalna"))
        self.pineappleBox.setText(_translate("Dialog", "ananas"))
        self.mushroomBox.setText(_translate("Dialog", "Pieczarka"))
        self.label.setText(_translate("Dialog", "Wybierz dodatki"))
        self.doublecheeseBox.setText(_translate("Dialog", "podwojny ser"))
        self.big.setText(_translate("Dialog", "Pizza duża"))
        self.salamiBox.setText(_translate("Dialog", "salami"))
        self.orderButton.setText(_translate("Dialog", "Zamow"))
        self.small.setText(_translate("Dialog", "Pizza mała"))
