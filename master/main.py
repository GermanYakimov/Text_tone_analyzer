# Copyright © 2017-2018. All rights reserved.
# Authors: German Yakimov, Aleksey Sheboltasov
# License: https://github.com/GermanYakimov/Text_tone_analyzer/blob/master/LICENSE
# Contacts: german@yakimov.su, alekseysheboltasov@gmail.com


import sys
import json
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication, QPushButton, QComboBox, QMainWindow
from modules.count_text_tonal.count_text_tonal import count_text_tonal
from PyQt5.QtGui import QFont, QIcon


class MainProgramWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.main()

    def config_count(self):
        with open('sys_info.json', 'r') as file:
            sys_info = json.load(file)

        if sys_info['input_method'] == 'Manually' and sys_info['output_method'] == 'File':
            self.config = 1
        if sys_info['input_method'] == 'Manually' and sys_info['output_method'] == 'Screen':
            self.config = 2
        if sys_info['input_method'] == 'Voice' and sys_info['output_method'] == 'File':
            self.config = 3
        if sys_info['input_method'] == 'Voice' and sys_info['output_method'] == 'Screen':
            self.config = 4
        if sys_info['input_method'] == 'File' and sys_info['output_method'] == 'File':
            self.config = 5
        if sys_info['input_method'] == 'File' and sys_info['output_method'] == 'Screen':
            self.config = 6

    def main(self):
        self.config_count()

        if self.config == 1:
            pass
        elif self.config == 2:
            pass
        elif self.config == 3:
            pass
        elif self.config == 4:
            pass
        elif self.config == 5:
            pass
        elif self.config == 6:
            pass

    # def initUI(self):
    #     self.setWindowIcon(QIcon('icon.ico'))
    #     self.qle = QLineEdit(self)
    #     self.qle.resize(350, 30)
    #     self.qle.move(75, 40)
    #     self.qle.setFont(QFont("Times", 14))
    #
    #     self.lbl = QLabel(self)
    #     self.lbl.move(50, 150)
    #     self.lbl.setFont(QFont("Times", 14))
    #     self.lbl.resize(300, 100)
    #
    #     self.btn = QPushButton("Посчитать тональность", self)
    #     self.btn.resize(180, 50)
    #     self.btn.move(150, 100)
    #     self.btn.clicked.connect(self.button_clicked)
    #     # self.btn.show()
    #
    #     self.setGeometry(500, 500, 500, 300)
    #     self.setWindowTitle('Sentiment Analyser')
    #     self.show()
    #
    # def button_clicked(self):
    #     tonal, weight = count_text_tonal(self.qle.text())
    #     self.lbl.setText('Text Tonal: ' + tonal + '\n' + 'Text Weight: ' + str(weight))


class SysInfGet(QWidget):
    def __init__(self):
        self.input_method = ''
        self.output_method = ''
        super().__init__()
        self.initUI()

    def get_input_text(self, text):
        self.input_method = text

    def get_output_text(self, text):
        self.output_method = text

    def ok_button_clicked(self):
        if (self.output_method == 'File' or self.output_method == 'Screen') and (self.input_method == 'Manually' or
                                                        self.input_method == 'File' or self.input_method == 'Voice'):
            if self.input_method == 'File' or self.output_method == 'File':
                self.get_file_info = FileInformationGet(self.input_method, self.output_method)
            else:
                sys_info = {'input_method': self.input_method, 'output_method': self.output_method}
                with open('sys_info.json', 'w') as file:
                    json.dump(fp=file, obj=sys_info, indent=4)
            self.close()
        else:
            self.err_label.setText('All fields must be fill in')
            self.err_label.show()

    def initUI(self):
        self.setWindowTitle('Sentiment Analyser')
        self.setWindowIcon(QIcon('icon.ico'))
        self.setGeometry(250, 250, 300, 250)

        # init a block to select an input method
        self.input_method_combo = QComboBox(self)
        self.input_method_combo.addItems(['...', 'Manually', 'Voice', 'File'])
        self.input_method_combo.move(200, 50)
        self.input_method_combo.setFont(QFont("Times", 12))

        self.label1 = QLabel(self)
        self.label1.setFont(QFont("Times", 12))
        self.label1.setText('Select the input method:')
        self.label1.move(10, 55)

        # init a block to select output method
        self.output_method_combo = QComboBox(self)
        self.output_method_combo.addItems(['...', 'Screen', 'File'])
        self.output_method_combo.move(200, 100)
        self.output_method_combo.setFont(QFont("Times", 12))

        self.label2 = QLabel(self)
        self.label2.setFont(QFont("Times", 12))
        self.label2.setText('Select the output method:')
        self.label2.move(10, 105)

        # init error label
        self.err_label = QLabel(self)
        self.err_label.setFont(QFont("Times", 11))
        self.err_label.setStyleSheet("QLabel {color:rgba(255, 99, 71, 255)}")
        self.err_label.resize(150, 30)
        self.err_label.move(90, 10)

        # init "OK" button
        self.ok_button = QPushButton("OK", self)
        self.ok_button.resize(150, 50)
        self.ok_button.move(75, 155)
        self.ok_button.clicked.connect(self.ok_button_clicked)

        self.show()
        self.input_method_combo.activated[str].connect(self.get_input_text)
        self.output_method_combo.activated[str].connect(self.get_output_text)


class FileInformationGet(QWidget):
    def __init__(self, input_method, output_method):
        super().__init__()
        self.input_method = input_method
        self.output_method = output_method
        self.input_filename = ''
        self.output_filename = ''
        self.config = 0
        self.initUI()

    def config_count(self):
        if self.input_method == 'File' and self.output_method == 'File':
            self.config = 1
        elif self.input_method == 'File' and self.output_method != 'File':
            self.config = 2
        elif self.output_method == 'File' and self.input_method != 'File':
            self.config = 3

    def ok_button_clicked(self):
        if self.config == 1:
            if self.qle1.text().endswith('.txt') and self.qle2.text().endswith('.txt'):
                self.input_filename = self.qle1.text()
                self.output_filename = self.qle2.text()
            else:
                self.err_label = QLabel(self)
                self.err_label.move(10, 10)
                self.err_label.resize(325, 30)
                self.setFont(QFont("Times", 10))
                self.err_label.setText("""All fields must be fill in (please, don't forget about ".txt")""")
                self.err_label.setStyleSheet("QLabel {color:rgba(255, 99, 71, 255)}")
                self.err_label.show()
                return ''

        elif self.config == 2:
            if self.qle.text().endswith('.txt'):
                self.input_filename = self.qle.text()
            else:
                self.err_label = QLabel(self)
                self.err_label.move(10, 10)
                self.err_label.resize(325, 30)
                self.setFont(QFont("Times", 10))
                self.err_label.setText("""All fields must be fill in (please, don't forget about ".txt")""")
                self.err_label.setStyleSheet("QLabel {color:rgba(255, 99, 71, 255)}")
                self.err_label.show()
                return ''

        elif self.config == 3:
            if self.qle.text().endswith('.txt'):
                self.output_filename = self.qle.text()
            else:
                self.err_label = QLabel(self)
                self.err_label.move(10, 10)
                self.err_label.resize(325, 30)
                self.setFont(QFont("Times", 10))
                self.err_label.setText("""All fields must be fill in (please, don't forget about ".txt")""")
                self.err_label.setStyleSheet("QLabel {color:rgba(255, 99, 71, 255)}")
                self.err_label.show()
                return ''

        sys_info = {'input_method': self.input_method,
                    'output_method': self.output_method,
                    'input_filename': self.input_filename,
                    'output_filename': self.output_filename}

        with open('sys_info.json', 'w') as file:
            json.dump(fp=file, obj=sys_info, indent=4)

        self.close()

    def initUI(self):
        self.config_count()

        if self.config == 1:
            self.setWindowTitle('Sentiment Analyser')
            self.setWindowIcon(QIcon('icon.ico'))
            self.setGeometry(300, 300, 350, 230)

            # elements for input file information read
            self.qle1 = QLineEdit(self)
            self.qle1.resize(130, 30)
            self.qle1.move(210, 40)
            self.qle1.setFont(QFont("Times", 10))

            self.lbl1 = QLabel(self)
            self.lbl1.move(10, 40)
            self.lbl1.setFont(QFont("Times", 11))
            self.lbl1.resize(200, 30)
            self.lbl1.setText('Enter name of the input file:')

            # elements for output file information read
            self.qle2 = QLineEdit(self)
            self.qle2.resize(130, 30)
            self.qle2.move(210, 90)
            self.qle2.setFont(QFont("Times", 10))

            self.lbl2 = QLabel(self)
            self.lbl2.move(10, 90)
            self.lbl2.setFont(QFont("Times", 11))
            self.lbl2.resize(200, 30)
            self.lbl2.setText('Enter name of the output file:')

            self.ok_btn = QPushButton("OK", self)
            self.ok_btn.resize(150, 50)
            self.ok_btn.move(100, 150)
            self.ok_btn.clicked.connect(self.ok_button_clicked)

        if self.config == 2:
            self.setWindowTitle('Sentiment Analyser')
            self.setWindowIcon(QIcon('icon.ico'))
            self.setGeometry(300, 300, 350, 180)

            # elements for input file information read
            self.qle = QLineEdit(self)
            self.qle.resize(130, 30)
            self.qle.move(210, 40)
            self.qle.setFont(QFont("Times", 10))

            self.lbl = QLabel(self)
            self.lbl.move(10, 40)
            self.lbl.setFont(QFont("Times", 11))
            self.lbl.resize(200, 30)
            self.lbl.setText('Enter name of the input file:')

            self.ok_btn = QPushButton("OK", self)
            self.ok_btn.resize(150, 50)
            self.ok_btn.move(100, 100)
            self.ok_btn.clicked.connect(self.ok_button_clicked)

        if self.config == 3:
            self.setWindowTitle('Sentiment Analyser')
            self.setWindowIcon(QIcon('icon.ico'))
            self.setGeometry(300, 300, 350, 180)

            # elements for output file information read
            self.qle = QLineEdit(self)
            self.qle.resize(130, 30)
            self.qle.move(210, 40)
            self.qle.setFont(QFont("Times", 10))

            self.lbl = QLabel(self)
            self.lbl.move(10, 40)
            self.lbl.setFont(QFont("Times", 11))
            self.lbl.resize(200, 30)
            self.lbl.setText('Enter name of the output file:')

            self.ok_btn = QPushButton("OK", self)
            self.ok_btn.resize(150, 50)
            self.ok_btn.move(100, 100)
            self.ok_btn.clicked.connect(self.ok_button_clicked)

        self.show()


class Main(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.main()

    def main(self):
        self.sys_inf_get = SysInfGet()
        self.sys_inf_get.close()


app = QApplication(sys.argv)
main = Main()
sys.exit(app.exec_())