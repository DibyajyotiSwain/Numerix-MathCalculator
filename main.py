import sys
from PySide6.QtWidgets import QApplication
from numerix.ui.pages import MainWindow
if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setApplicationName('NUMERIX')
    window=MainWindow(); window.show()
    sys.exit(app.exec())
