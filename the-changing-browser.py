from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        tool_bar = QToolBar()

        tool_bar.setIconSize(QSize(24, 24))

        self.addToolBar(tool_bar)
        homeButton = QAction(QIcon("home.png"), 'Click to open Home page', self)
        homeButton.triggered.connect(self.home)
        tool_bar.addAction(homeButton)
        backButton = QAction(QIcon("backward.png"), 'Click to go back', self)
        backButton.triggered.connect(self.browser.back)
        tool_bar.addAction(backButton)
        fwdButton = QAction(QIcon("forward.png"), 'Click to go forward', self)
        fwdButton.triggered.connect(self.browser.forward)
        tool_bar.addAction(fwdButton)
        refreshButton = QAction(QIcon("refresh.png"), 'Refresh', self)
        refreshButton.triggered.connect(self.browser.reload)
        tool_bar.addAction(refreshButton)
        self.url_entry = QLineEdit()
        self.url_entry.returnPressed.connect(self.take_url)
        tool_bar.addWidget(self.url_entry)
        self.browser.urlChanged.connect(self.update_url)

    def home(self):
        pass
        self.browser.setUrl(QUrl('https://duckduckgo.com'))

    def take_url(self):
        url = self.url_entry.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, entered_url):
        self.url_entry.setText(entered_url.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('The Changing Browser')
window = MainWindow()
app.exec_()