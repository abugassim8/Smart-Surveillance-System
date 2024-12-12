import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QCompleter, QGridLayout, QLineEdit, QWidget


class LineEdit(QLineEdit):
    def __init__(self, mapping, parent=None):
        super(LineEdit, self).__init__(parent)

        self.mapping = mapping

    def keyPressEvent(self, event):
        last_text = self.text()
        super(LineEdit, self).keyPressEvent(event)
        new_text = self.text()
        if last_text + event.text() == new_text:
            new_text = self.mapping.get(event.text())
            if new_text is not None:
                self.setText(last_text + new_text)


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        layout = QGridLayout(self)

        names = ["Apple", "Alps", "Berry", "Cherry"]
        completer = QCompleter(names)

        mapping = {"<": "less than", ">": "greater than", "'": "`"}
        self.lineedit = LineEdit(mapping)
        self.lineedit.setCompleter(completer)
        layout.addWidget(self.lineedit, 0, 0)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())