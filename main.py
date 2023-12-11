import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QPlainTextEdit, QVBoxLayout, QWidget, QMessageBox

from ml import Ui_MainWindow
from constants import READ_ONLY, TITLE
from checkTitle import checkTitles
from checkIndent import checkIndents


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # начальные значения
        self.pathFile = ''
        self.currentTitle = self.ui.titlePicked
        self.ui.filePicked.setText('Файл не выбран.')

        # события кнопок
        self.ui.pickFileButton.clicked.connect(self.pickFileButton_Clicked)
        self.ui.checkFile.clicked.connect(self.checkFile_Clicked)
        self.ui.choiceTitle.activated.connect(self.choiceTitleActive)
        self.ui.enterIndent.textEdited.connect(self.changeIndentLabel)

        self.ui.choiceTitle.addItems(TITLE.keys())
        self.ui.titlePicked.setText(self.ui.choiceTitle.currentText())

        self.plain_text = QPlainTextEdit()
        self.plain_text.setReadOnly(READ_ONLY)

        layout = QVBoxLayout()
        layout.addWidget(self.plain_text)

        w = QWidget()
        w.setLayout(layout)
        self.ui.answer.setWidget(w)

        self.setWindowTitle("ML title")

    def changeIndentLabel(self, text):
        self.ui.enterIndentLabel.setText(text + ' см')

    def choiceTitleActive(self, index):
        self.ui.titlePicked.setText(self.ui.choiceTitle.itemText(index))
        self.currentTitle = self.ui.titlePicked

    def pickFileButton_Clicked(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         '.',
                                                         'Word files (*.docx)')
        if filename == '':
            self.ui.filePicked.setText('Файл не выбран.')
            self.pathFile = ''
        else:
            self.pathFile = filename
            filename = filename.split('/')[-1]
            self.ui.filePicked.setText(filename)

    def checkFile_Clicked(self):
        if self.pathFile == '':
            try:
                self.notSelectFile = QMessageBox()
                self.notSelectFile.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                self.notSelectFile.setText('Вы не выбрали файл!')
                self.notSelectFile.setWindowTitle('Ошибка!')
                self.notSelectFile.setIcon(QMessageBox.Warning)
                res = self.notSelectFile.exec()
            except Exception as e:
                pass
        else:
            if self.ui.enterIndent.text() == '':
                self.ui.enterIndent.setText('0')
            text = checkIndents(self.ui.enterIndent.text(), self.pathFile)
            text += checkTitles(self.currentTitle.text(), self.pathFile)
            self.plain_text.setPlainText(text)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()