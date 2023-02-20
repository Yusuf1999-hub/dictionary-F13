from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QPushButton

class Oyna(QWidget):
    def __init__(self):
        super().__init__()

        self.listWDG = QListWidget(self)
        self.listWDG.addItem("Salom")
        self.listWDG.addItem("Salom")
        self.listWDG.addItem("Salom")
        self.listWDG.addItem("Salom")
        self.listWDG.addItem("Salom")
        self.listWDG.addItem("Salom")
        self.listWDG.addItems(["asdfasf","asdfasf","qweqr","pojzlxckv","igoqwrhkljfn","wioheflzxnv;sjif"])


app = QApplication([])
win = Oyna()
win.show()
app.exec_()