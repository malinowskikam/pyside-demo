import sys

from PySide6.QtWidgets import QApplication

from pyside_demo.main_widget import MainWidget


def main():
    app = QApplication(sys.argv)

    widget = MainWidget()
    widget.show()

    app.exec()

if __name__ == "__main__":
    main()