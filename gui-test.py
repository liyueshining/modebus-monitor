import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPalette, QColor
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget, QGridLayout, QHBoxLayout, QStackedLayout, QToolBar, QStatusBar, QDialog, QDialogButtonBox,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for widget in widgets:
            layout.addWidget(widget())

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainLayoutWindow(QMainWindow):

    def __init__(self):
        super(MainLayoutWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

class MainGridLayoutWindow(QMainWindow):

    def __init__(self):
        super(MainGridLayoutWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()

        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('purple'), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class MainMixedLayoutWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        btn = QPushButton("red")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("red"))

        btn = QPushButton("green")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("green"))

        btn = QPushButton("yellow")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("yellow"))

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)


class MainToolBarWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(20, 20))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("icons/plug-connect-16.png"), "Connect", self)
        button_action.setStatusTip("This is your connect button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        button_action_reset = QAction(QIcon("icons/reset-16.png"), "Reset", self)
        button_action_reset.setStatusTip("This is your reset button")
        button_action_reset.triggered.connect(self.onMyToolBarButtonClick)
        button_action_reset.setCheckable(True)
        toolbar.addAction(button_action_reset)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("icons/ethernet-port-16.png"), "ModbusTCP", self)
        button_action2.setStatusTip("This is your ModbusTCP setting button")
        button_action2.triggered.connect(self.onTcpSettingButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        button_action3 = QAction(QIcon("icons/serial-pot-16.png"), "ModbusRTU", self)
        button_action3.setStatusTip("This is ModbusRTU setting button")
        button_action3.triggered.connect(self.onRtuSettingButtonClick)
        button_action3.setCheckable(True)
        toolbar.addAction(button_action3)

        toolbar.addSeparator()

        toolbar.addWidget(QLabel("Modebus Mode: "))

        mode = QComboBox()
        mode.addItems(["TCP", "RTU"])
        toolbar.addWidget(mode)

        self.setStatusBar(QStatusBar(self))

    def onTcpSettingButtonClick(self, s):
        print("click", s)
        dlg = TcpSettingDialog(self)
        dlg.exec()

    def onRtuSettingButtonClick(self, s):
        print("click", s)
        dlg = RtuSettingDialog(self)
        dlg.exec()

    def onMyToolBarButtonClick(self, s):
        print("click", s)


class TcpSettingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Modbus TCP Setting")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        gridlayout_tcp_setting = QGridLayout()

        label_ip = QLabel("IP")
        lineedit_ip = QLineEdit()
        lineedit_ip.setInputMask("000.000.000.000")
        lineedit_ip.setText("127.000.000.001")

        label_port = QLabel("TCP Port")
        lineedit_port = QLineEdit()
        lineedit_port.setText("502")

        gridlayout_tcp_setting.addWidget(label_ip, 0, 0)
        gridlayout_tcp_setting.addWidget(lineedit_ip, 0, 1)
        gridlayout_tcp_setting.addWidget(label_port, 1, 0)
        gridlayout_tcp_setting.addWidget(lineedit_port, 1, 1)

        self.layout.addLayout(gridlayout_tcp_setting)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class RtuSettingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Modbus RTU Setting")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        gridlayout_tcp_setting = QGridLayout()

        label_device = QLabel("Serial device")
        label_port = QLabel("Serial port")
        label_baud = QLabel("Baud")
        label_databits = QLabel("Data Bits")
        label_stopbits = QLabel("Stop Bits")
        label_Parity = QLabel("Parity")

        combobox_device = QComboBox()
        combobox_device.addItems(["/dev/ttyS", "/dev/ttyUSB"])
        combobox_device.setEditable(True)
        #combobox_device.setCurrentIndex(-1)
        combobox_device.lineEdit().setPlaceholderText("COM")

        spinbox_port = QSpinBox()
        spinbox_port.setMinimum(1)
        spinbox_port.setMaximum(65535)
        spinbox_port.setValue(1)

        combobox_baud = QComboBox()
        combobox_baud.addItems(["1200", "2400", "4800", "9600", "19200", "38400", "57600", "115200"])
        combobox_baud.setCurrentIndex(3)

        combobox_databits = QComboBox()
        combobox_databits.addItems(["7", "8"])
        combobox_databits.setCurrentIndex(1)

        combobox_stopbits = QComboBox()
        combobox_stopbits.addItems(["1", "1.5", "2"])
        combobox_stopbits.setCurrentIndex(0)

        combobox_parity = QComboBox()
        combobox_parity.addItems(["None", "Odd", "Even"])
        combobox_parity.setCurrentIndex(0)

        gridlayout_tcp_setting.addWidget(label_device, 0, 0)
        gridlayout_tcp_setting.addWidget(combobox_device, 0, 1)
        gridlayout_tcp_setting.addWidget(label_port, 1, 0)
        gridlayout_tcp_setting.addWidget(spinbox_port, 1, 1)
        gridlayout_tcp_setting.addWidget(label_baud, 2, 0)
        gridlayout_tcp_setting.addWidget(combobox_baud, 2, 1)
        gridlayout_tcp_setting.addWidget(label_databits, 3, 0)
        gridlayout_tcp_setting.addWidget(combobox_databits, 3, 1)
        gridlayout_tcp_setting.addWidget(label_stopbits, 4, 0)
        gridlayout_tcp_setting.addWidget(combobox_stopbits, 4, 1)
        gridlayout_tcp_setting.addWidget(label_Parity, 5, 0)
        gridlayout_tcp_setting.addWidget(combobox_parity, 5, 1)

        self.layout.addLayout(gridlayout_tcp_setting)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


app = QApplication(sys.argv)
window = MainToolBarWindow()
window.show()
app.exec()