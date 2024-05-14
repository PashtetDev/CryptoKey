import sys
from ui_resources_new.main_window_ui import *


class KeyManager(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mainBtn.clicked.connect(self.open_main_panel)
        self.ui.settingBtn.clicked.connect(self.open_main_panel)
        self.ui.managerBtn.clicked.connect(self.open_main_panel)

        self.ui.quitBtn.clicked.connect(self.open_general_window)
        self.ui.regBtn.clicked.connect(self.open_general_window)
        self.ui.loginBtn.clicked.connect(self.open_general_window)
        self.ui.signupBtn.clicked.connect(self.open_general_window)
        self.ui.toExitBtn.clicked.connect(self.open_general_window)

    def open_main_panel(self):
        sender = self.sender().objectName()
        sizeX = 500
        if sender == "mainBtn":
            self.ui.mainPage.setMinimumSize(sizeX, 0)
            self.ui.settings.setMinimumSize(0, 0)
            self.ui.passwordManager.setMinimumSize(0, 0)
        elif sender == "settingBtn":
            self.ui.mainPage.setMinimumSize(0, 0)
            self.ui.settings.setMinimumSize(sizeX, 0)
            self.ui.passwordManager.setMinimumSize(0, 0)
        else:
            self.ui.mainPage.setMinimumSize(0, 0)
            self.ui.settings.setMinimumSize(0, 0)
            self.ui.passwordManager.setMinimumSize(sizeX, 0)

    def open_general_window(self):
        sender = self.sender().objectName()
        sizeX = 500
        max = 16777215

        self.ui.general.setMaximumSize(0, 0)
        self.ui.loginMenu.setMaximumSize(0, 0)
        self.ui.regMenu.setMaximumSize(0, 0)

        if sender == "quitBtn" or sender == "regBtn" or sender == "toExitBtn":
            self.ui.general.setMinimumSize(0, 0)
            self.ui.loginMenu.setMaximumSize(max, max)
            self.ui.loginMenu.setMinimumSize(sizeX, 0)
            self.ui.regMenu.setMinimumSize(0, 0)
        elif sender == "loginBtn":
            self.ui.general.setMaximumSize(max, max)
            self.ui.general.setMinimumSize(sizeX, 0)
            self.ui.loginMenu.setMinimumSize(0, 0)
            self.ui.regMenu.setMinimumSize(0, 0)
        else:
            self.ui.general.setMinimumSize(0, 0)
            self.ui.loginMenu.setMinimumSize(0, 0)
            self.ui.regMenu.setMaximumSize(max, max)
            self.ui.regMenu.setMinimumSize(sizeX, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KeyManager()
    window.show()

    sys.exit(app.exec())