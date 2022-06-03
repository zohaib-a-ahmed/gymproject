import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar
from PyQt6.QtGui import QFont, QPixmap, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Progress Pal")
        self.setMaximumSize(1200, 700)
        self.setMinimumSize(900,500)

        self.createTools()
        self.createBackground()
        self.setStatusBar(QStatusBar(self))

    def createBackground(self):
        background = QLabel()
        background.setPixmap(QPixmap('barbellsimple.jpeg'))
        background.setScaledContents(True)
        self.setCentralWidget(background)
    
    def createTools(self):
        menu = QToolBar()
        self.addToolBar(menu)

        chestbutton = QAction("Chest", self)
        chestbutton.setStatusTip("Push Day")
        chestbutton.triggered.connect(self.onMyToolBarButtonClick)
        menu.addAction(chestbutton)

        pushbutton = QAction("Back", self)
        pushbutton.setStatusTip("Push Day")
        pushbutton.triggered.connect(self.onMyToolBarButtonClick)
        menu.addAction(pushbutton)

        pushbutton = QAction("Legs", self)
        pushbutton.setStatusTip("Push Day")
        pushbutton.triggered.connect(self.onMyToolBarButtonClick)
        menu.addAction(pushbutton)

        pushbutton = QAction("Shoulders", self)
        pushbutton.setStatusTip("Push Day")
        pushbutton.triggered.connect(self.onMyToolBarButtonClick)
        menu.addAction(pushbutton)

        pushbutton = QAction("Triceps", self)
        pushbutton.setStatusTip("Push Day")
        pushbutton.triggered.connect(self.onMyToolBarButtonClick)
        menu.addAction(pushbutton)

        pushbutton = QAction("Biceps", self)
        pushbutton.setStatusTip("Push Day")
        pushbutton.triggered.connect(self.onMyToolBarButtonClick)
        menu.addAction(pushbutton)

    def onMyToolBarButtonClick(self, s):
        print("click", s)
        



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()