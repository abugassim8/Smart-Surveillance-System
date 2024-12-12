import sys
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QLineEdit,
    QTextBrowser,
    QCompleter,
)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("console")
        self.setGeometry(10, 50, 500, 800)

        # Create text box for input
        self.consoleCommandLineEdit = QLineEdit()
        self.consoleCommandLineEdit.setFixedHeight(25)
        self.consoleCommandLineEdit.editingFinished.connect(self.gotConsoleCommand)

        self.model = QStandardItemModel()
        self.model.appendRow([QStandardItem(text) for text in ("aaa1", "aaa2", "aaa3")])
        completer = QCompleter(self.model, self)
        self.consoleCommandLineEdit.setCompleter(completer)

        # Create text box for output
        self.consoleViewer = QTextBrowser(lineWrapMode=QTextBrowser.NoWrap)

        widget = QWidget()
        self.setCentralWidget(widget)
        vlay = QVBoxLayout(widget)
        vlay.addWidget(self.consoleCommandLineEdit)
        vlay.addWidget(self.consoleViewer)

    def gotConsoleCommand(self):
        cmd = self.consoleCommandLineEdit.text()
        self.consoleCommandLineEdit.clear()
        self.sendCommandToConsole(cmd)

    def sendCommandToConsole(self, cmd):
        self.consoleViewer.append(cmd)  # add cmd to output box
        if not self.model.findItems(cmd):
            self.model.appendRow(QStandardItem(cmd))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())