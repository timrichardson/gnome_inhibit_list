from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
import importlib.resources as pkg_resources

# Maximum number of inhibitors we'll bother to display.
# If you have more than 5 apps preventing sleep.. you have some bigger problems.
MAX_INHIBITORS = 5
pkg_path = pkg_resources.files('list_session_inhibitors')


class TrayHandler:

    inhibitors = []

    def __init__(self):
        self.app = QApplication([])
        self.app.setQuitOnLastWindowClosed(False)
        self.tray = QSystemTrayIcon()
        self.set_icon("uninhibited.png")

        self.tray.setVisible(True)

        # Creating the options
        self.menu = QMenu()

        # To quit the app
        self.quit = QAction("Quit")
        self.quit.triggered.connect(self.app.quit)

        # Generate all menu items up front. This way we're not thrashing by adding/removing them constantly.
        for i in range(0, MAX_INHIBITORS):
            inhib = QAction("n/a")
            inhib.setEnabled(False)
            # inhib.setVisible(False)
            self.inhibitors.append(inhib)
            self.menu.addAction(self.inhibitors[i])

        self.menu.addAction(self.quit)

        # Adding options to the System Tray
        self.tray.setContextMenu(self.menu)

    def set_icon(self, icon_name):
        # Adding an icon
        icon_name = os.path.join(pkg_path, icon_name)
        icon = QIcon(icon_name)

        # Adding item on the menu bar
        self.tray.setIcon(icon)

    def set_inhibitors(self, inhib_tips):
        for i in range(0, MAX_INHIBITORS):
            if i >= len(inhib_tips):
                self.inhibitors[i].setText("n/a")
                self.inhibitors[i].setVisible(False)
            else:
                self.inhibitors[i].setText(inhib_tips[i])
                self.inhibitors[i].setVisible(True)

    def run(self):
        self.app.exec_()
